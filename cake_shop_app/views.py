from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from cake_shop_app.core.mixins import AnyGroupRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from cake_shop_app.models import Product, Order, OrderItem


class IndexView ( ListView ):
    template_name = 'index.html'
    model = Product
    context_object_name = 'cakes'
    paginate_by = 5

# @login_required(login_url=reverse_lazy('sign in'))
# @any_group_required(groups=['User'])
# def create(request):
#     if request.method == 'GET':
#         form = ProductCreateForm()
#         return render(request, 'create.html', {'form': form})
#     else:
#         form = ProductCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#         return render(request, 'create.html', {'form': form})

class ProductCreateView ( AnyGroupRequiredMixin, CreateView ):
    template_name = 'create.html'
    model = Product
    fields = '__all__'
    success_url = reverse_lazy ( 'index' )


class ProductView ( DetailView ):
    model = Product
    template_name = "cake_shop\product.html"
    context_object_name = "cake"


class ProductUpdateView ( AnyGroupRequiredMixin, UpdateView ):
    template_name = 'edit.html'
    model = Product
    fields = '__all__'
    context_object_name = "cake"
    success_url = reverse_lazy ( 'index' )


class ProductDeleteView ( AnyGroupRequiredMixin, DeleteView ):
    template_name = 'delete.html'
    model = Product
    success_url = reverse_lazy ( 'index' )

    def delete(self, request, *args, **kwargs):
        item = self.get_object()
        order_qs = Order.objects.all ().exclude(complete=True)
        for order in order_qs:
            if item.id == order.items.values('item_id').first()['item_id']:
                messages.warning(request, "The product is in active order! You cannot delete it")
                return redirect("index")
        self.object = self.get_object()
        success_url = self.get_success_url()
        item.delete()
        return HttpResponseRedirect(success_url)

def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item = item,
        user = request.user,
    )

    order_qs = Order.objects.filter(user=request.user,complete=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.success(request, "Added quantity Item")
            return redirect("index")
        else:
            order.items.add(order_item)
            messages.success(request, "Item added to your cart")
            return redirect("index")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, date_ordered=ordered_date)
        order.items.add(order_item)
        messages.success(request, "Item added to your cart")
        return redirect("index")

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, complete=False)
            context = {
                'object': order
            }
            return render(self.request, 'cart/cart.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("index")


def complete_order(request):
    order = Order.objects.filter(user=request.user,complete=False)
    order_to_complete = get_object_or_404(Order, pk=order[0].id)
    order_to_complete.complete = True
    order_to_complete.save()
    messages.success(request, "Your order has been accepted. We will contact you for details ")
    return redirect("index")

def about_us(request):
    return render(request, 'common/about_us.html')

def contacts(request):
    return render(request, 'common/contacts.html')

def home_page(request):
    return render(request, 'home.html')

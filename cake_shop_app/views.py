from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
import json

from django.utils import timezone
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth import mixins as auth_mixins
from cake_shop_app.core.mixins import AnyGroupRequiredMixin
from django.urls import reverse_lazy, reverse
# from cake_shop_app.core.decorators import any_group_required
# from cake_shop_app.forms import ProductCreateForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from cake_shop_app.models import Product, Order, OrderItem
from cake_shop_auth.models import CakeShopUser


class IndexView ( ListView ):
    template_name = 'index.html'
    model = Product
    context_object_name = 'cakes'
    paginate_by = 3

# @login_required(login_url=reverse_lazy('sign in'))
# @any_group_required(groups=['User']) #'Staff'
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

def add_to_cart(request, pk):
    # взема продукта и прави обект OrderItemCreateView(CreateView)
    # проверява дали има този юзер поръчка неизпълнена и ако няма - прави OrderCreateView(CreateView) и добавя продукта
    # ако има - добавя продукта към съществуващата поръчка
    # извиква страница на която се визуализира цялата поръчка
    # извиква страница на която се визуализира цялата поръчка

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
            messages.info(request, "Added quantity Item")
            return redirect("index")
        else:
            order.items.add(order_item)
            messages.info(request, "Item added to your cart")
            return redirect("index")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, date_ordered=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")
        return redirect("index")


class OrderCreateView(CreateView):
    model = Order
    template_name = 'cart/create-order.html'
    fields = '__all__'
    object = None

    def get_success_url(self):
        return reverse ('create item', kwargs={
            'pk':self.object.id
        })


class OrderItemCreateView(CreateView):
    model = OrderItem
    template_name = 'cart/create-item.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse ('details item', kwargs={
            'pk':self.object.id
        })

class OrderListView(ListView):
    model = Order
    template_name = 'cart/list-orders.html'


class OrderItemDetailView(SingleObjectMixin,ListView ):
    model = OrderItem
    template_name = 'cart/details-item.html'
    object = None
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=OrderItem.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = self.object
        return context

    def get_queryset(self):
        return self.object.order_set.all()

class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'cart/list-items.html'

    # template_name = 'cake_shop\cart_items.html'
    #
    # def get_queryset(self):
    #     self.order = get_object_or_404(Order, name=self.kwargs['id'])
    #     return OrderItem.objects.filter(order=self.order)




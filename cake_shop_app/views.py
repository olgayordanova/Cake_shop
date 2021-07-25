from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone

from cake_shop_app.core.decorators import any_group_required
from cake_shop_app.forms import ProductCreateForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from cake_shop_app.models import Product

from cake_shop_app.models import Product
# def index(request):
#     cakes = Product.objects.all()
#     return render(request, 'index.html', {'cakes': cakes})

from cake_shop_app.core.mixins import AnyGroupRequiredMixin


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'cakes'
    paginate_by = 10


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

class ProductCreateView(AnyGroupRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('index')

class ProductView(DetailView):
    model = Product
    template_name = "cake_shop\product.html"
    context_object_name = "cake"

class ProductUpdateView(AnyGroupRequiredMixin, UpdateView):
    template_name = 'edit.html'
    model = Product
    fields = '__all__'
    context_object_name = "cake"
    success_url = reverse_lazy('index')

class ProductDeleteView(AnyGroupRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Product
    success_url = reverse_lazy('index')
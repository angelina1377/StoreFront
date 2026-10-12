from django.views.generic import ListView, DetailView, CreateView
from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 9  # заменяет пагинацию из старого FBV

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = '/catalog/'  # или reverse_lazy('catalog:product_list'), если настроишь app_name корректно

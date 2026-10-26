from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Product
from .forms import ProductForm

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})


@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # ИСПРАВЛЕНИЕ: Проверяем право на ИЗМЕНЕНИЕ (change), а не удаление (delete)
    if not (product.owner == request.user or request.user.has_perm('catalog.change_product')):
        raise PermissionDenied

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'catalog/product_form.html', {'form': form})


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not (product.owner == request.user or request.user.has_perm('catalog.delete_product')):
        raise PermissionDenied
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'catalog/product_confirm_delete.html', {'product': product})

@login_required
def toggle_publish(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not (product.owner == request.user or request.user.has_perm('catalog.can_unpublish_product')):
        raise PermissionDenied
    product.is_published = not product.is_published
    product.save()
    return redirect('product_detail', pk=product.pk)

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

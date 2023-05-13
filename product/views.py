from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import product, Logo
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator


# Create your views here.
def products(request):
    l0g0 = Logo.objects.get(pk=1)
    page_obj = product0 = product.objects.values('id','img','name','seller_name','price','description')
    product_name = request.GET.get('product_name')
    if product_name != '' and product_name is not None:
        page_obj = product0.filter(name__icontains = product_name)
    paginator = Paginator(page_obj, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj":page_obj,
               "logo":l0g0}
    return render(request, "product/index.html", context)

#classbasedview
class ProductClassBasedView(ListView):
    model = product
    template_name = "product/index.html"
    context_object_name = "item"
    extra_context = {"logo":Logo.objects.get(pk=1)}
    paginate_by = 3


def product_detail(request, id):
    product_details = product.objects.get(id=id)
    context = {"product_detail":product_details}
    return render(request, "product/Product_detail.html", context)

#ClassBasedDetailView
class ProductClassBasedDetailView(DetailView):
    model = product
    template_name = "product/Product_detail.html"
    context_object_name = "product_detail"

@login_required
def AddProduct(request):
    if request.method == "POST":
        seller_name = request.user
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('description')
        specs = request.POST.get('specs')
        image = request.FILES['upload']
        item = product(seller_name=seller_name, name=name, price=price, description=desc, specs=specs, img=image)
        item.save()
    return render(request,"product/AddProduct.html")


#ClassBasedCreateView for adding products
class AddClassBasedView(CreateView):
    model = product
    fields = ['seller_name', 'name', 'price', 'description', 'specs', 'img']
    success_url = '/product/'              #it's redirect url


@login_required
def UpdateProduct(request, id):
    Product = product.objects.get(id=id)
    if request.method == "POST":
        Product.name = request.POST.get('name')
        Product.price = request.POST.get('price')
        Product.description = request.POST.get('description')
        Product.specs = request.POST.get('specs')
        Product.img = request.FILES['upload']
        Product.save()
        return redirect('/product')
    context = {'product':Product}
    return render(request, "product/Edit_product.html",context)


#ClassBasedCreateView for deleting products
@method_decorator(login_required, name='dispatch')
class DeleteClassBasedView(DeleteView):
    model = product
    success_url = reverse_lazy("product:products")


#ClassBasedUpdateView for updating products
@method_decorator(login_required, name='dispatch')
class UpdateClassBasedView(UpdateView):
    model = product
    fields = ['seller_name', 'name', 'price', 'description', 'specs', 'img']
    success_url = reverse_lazy("product:products")

@login_required
def DeleteProduct(request, id):
    Product = product.objects.get(id=id)
    context = {"Product":Product}
    if request.method == "POST":
        Product.delete()
        return redirect('/product')
    return render(request, "product/DeleteProduct.html", context)


def my_listings(request):
    pr0duct = product.objects.filter(seller_name=request.user)
    context = {
        "product":pr0duct
    }
    return render(request, "product/mylistings.html", context)

























































from django.http import  Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product

# Create your views here.



def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    #POST request
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect("home")
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)
    
def dynamic_lookup_view(request,id):
    # obj = Product.objects.get(id=id);
    obj = get_object_or_404(Product, id = id)
    # obj = Product.objects.get(id=id)
    # try:
    #     obj =Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)



def render_initial_data(request):
    initial_data = {
        'title': "My this awesome title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             # Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST) 
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title) 
#     context = {}
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST) 
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title) 
#     context = {}
#     return render(request, "products/product_create.html", context)

#     context = {}
#     return render(request, "products/product_create.html", context)



def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)



def product_datail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title':obj.title,
    #     'description':obj.description
    # }
    context ={
        "object" : obj
    }
    return render(request,"products/product_detail.html",context)
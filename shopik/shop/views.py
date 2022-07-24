from django.shortcuts import render
from .models import Category, Products, Basket


def home(request, slug=None):
    context = {
        "categories": Category.objects.all(),

    }
    if slug == None:
        context["products"] = Products.objects.all()
    else:
        context["products"] = Products.objects.filter(category=slug)
    return render(request, "shopik/home.html", context)

def product_detail(request,id):
    print(id)
    print(request.POST)
    if request.POST:
        basket = Basket(product=Products.objects.get(id=id), count= request.POST['count'])
        basket.save()
    context = {
        'product': Products.objects.get(id=id)
    }
    return render(request, 'shopik/product_detail.html', context)

def basket(request):
    context = {
        'products': Basket.objects.all(),
        'product': Products,
    }
    return render(request,'shopik/basket.html',context)
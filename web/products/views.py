from django.shortcuts import render,redirect
from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def product_detail(request,id):
    product=Product.objects.get(product_id=id)
    return render(request, 'product_detail.html',{'product':product})


def create_product(request):
    if request.method=='POST':
        product= Product.objects.create(
        product_id=request.POST['product_id'],
        name=request.POST['name'],
        category=request.POST['category'],
        price=request.POST['price'],
        description=request.POST['description'],
        stock_quantity=request.POST['stock_quantity'],
        image = request.FILES['image'])
        return render(request,'product_detail.html',{'product':product})

    return render(request,'add_product.html')

def update_product(request, id):

    product = Product.objects.get(product_id=id)

    if request.method == 'POST':

        product.name = request.POST['name']
        product.category = request.POST['category']
        product.price = request.POST['price']
        product.description = request.POST['description']
        product.stock_quantity = request.POST['stock_quantity']

        image = request.FILES.get('image')

        if image:
            product.image = image

        product.save()

        return redirect('product_detail', id=product.product_id)

    return render(request, 'update_product.html', {'product': product})


from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Bins,complaintpost,Feed_back,product,Cart

from django.db.models import Q
def hom(request):
    return render(request, 'index.html')
def registration(request):
    return render(request, 'registration.html')
def registration1(request):
    return render(request, 'registration1.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def base(request):
    return render(request, 'base.html')
def service(request):
    return render(request, 'services.html')
def home1(request):
    return render(request, 'home1.html')
def home2(request):
    return render(request, 'home2.html')
def driverregistration(request):
    return render(request, 'driverreg.html')
def complaint(request):
    return render(request,'complaint.html')
def cart(request):
    return render(request,'cart.html')

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        feedbacktype = request.POST.get("feedbacktype")
        des_feedback = request.POST.get("des_feedback")
        print(name, email, feedbacktype,des_feedback)
        rev =Feed_back.objects.create(name=name,email=email,feedbacktype=feedbacktype,des_feedback=des_feedback)
        rev.save()

    return render(request,'feedback.html')


def Views_bin(request):
    viewbin = Bins.objects.all()

    return render(request,"see.html",{'Bins':viewbin})

def products(request):
    product_value = product.objects.all()

    return render(request,"shopping.html",{'product':product_value})

def Complaint(request):
    print('2')
    if request.method == 'POST':
        print('1')
        # c_fname= request.POST.get("c_fname",True)
        c_landmark= request.POST.get("c_landmark",True)
        bin_number= request.POST.get("bin_number",True)
        c_complant= request.POST.get("c_complant",True)
        print(c_landmark,bin_number,c_complant)
        ins = complaintpost(c_landmark=c_landmark,bin_number=bin_number,c_complant=c_complant)
        print(ins)
        ins.save()
        print("The data has been written to the db")
        return render(request,'home2.html')
    else:
        return render(request, 'complaint.html')


def searchbar(request):
    if request.method=='GET':

        keyword = request.GET.get('keyword')
        print(keyword)

        if keyword:

            products =Bins.objects.all().filter(Q(Bin_name__icontains=keyword) | Q(Bin_location__region__icontains=keyword))
            print(products)

            product_count = products.count()
            print(product_count)
            return render(request,'searchbar.html',{'products':products})

import requests
def get_news(request):
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=e92090481bc24996a2a89b1f90299cdf'
    response = requests.get(url)
    articles = response.json()['articles']
    return render(request, 'news.html', {
                    "page": "Newsplatform",
                    "articles": articles
                })

def addcart(request,id):
    print(id)
    user = request.user
    print(user)
    item = product.objects.get(prd_id=id)


    if Cart.objects.filter(products_id=item).exists():
        cart = Cart.objects.all()
        context = {'newcart': cart}
        return render(request, 'cart.html', context)
    else:
        product_qty = 1
        price = item.prd_price * product_qty
        new_cart = Cart(products_id=id,product_qty=product_qty, price=price)
        new_cart.save()
        cart=Cart.objects.all()
        context={'newcart':cart}
        return render(request,'cart.html',context)
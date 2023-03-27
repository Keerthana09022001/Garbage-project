from django.http import HttpResponse
from django.shortcuts import render
from .models import Bins,complaintpost,Feed_back
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
def product(request):
    return render(request,'products.html')

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

    # context = {
    #
    #     'results': products,
    #
    #     'product_count': product_count,
    #
    # }
    #
    # return render(request, 'searchbar.html', context)
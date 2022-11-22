from django.http import HttpResponse
from django.shortcuts import render
from .models import Bins,complaintpost
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
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            Bin_name = Bins.objects.filter(Bin_name__icontains=query)
            return render(request, 'searchresult.html', {'Bin_name':Bin_name})
        else:
            print("No information to show")
            return render(request, 'searchbar.html', {})

def searchresult(request):
    return render(searchresult,'searchresult.html')
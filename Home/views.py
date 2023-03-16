from django.http import HttpResponse
from django.shortcuts import render
from .models import Bins,complaintpost,Feed_back
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


#
# def create_superuser(self, password, email, **extra_fields):
#     user = self.create_user(
#         email=self.normalize_email(email),
#         password=password, **extra_fields
#
#     )
#     user.is_admin = True
#     user.is_active = True
#     user.is_staff = True
#     user.is_superadmin = True
#     user.save(using=self._db)
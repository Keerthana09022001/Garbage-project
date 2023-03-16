
#from ast import Not
#from turtle import home
from django.shortcuts import render
from django.contrib import messages,auth
from django.contrib.auth.models import auth
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from .models import Account
from django.views.decorators.cache import cache_control
import razorpay



# from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.

def index(request):
    return render(request,'index.html')
def base(request):
    return render(request,'base.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
def registration(request):
    return render(request,'registration1.html')
def home2(request):
    return render(request,'home2.html')
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mob = request.POST['phone']
        address = request.POST['address']
        pincode = request.POST['pincode']
        state = request.POST['state']
        district = request.POST['district']
        land_mark = request.POST['land_mark']
        role = request.POST.get('role')
        password = request.POST['password']
        is_customer=False
        if role=='is_customer':
            is_customer=True
        if Account.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return redirect('registration1')
        else:
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,  land_mark=land_mark, address=address, pincode=pincode, state=state, district=district, contact=mob, role=role, password=password, is_customer=is_customer)
            user.save()
            messages.success(request, 'Thank you for registering with us')
            # return redirect('login')
            return redirect('payment_page')

    else:
        return render(request,'registration1.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        user=authenticate(email=email,password=password)
        print(user)
        if user is not None:
            #login(user)
            auth.login(request, user)
            # save email in session
            request.session['email'] = email
            if user.is_customer:
                return redirect('home2')
            elif user.is_admin:
                 return redirect('http://127.0.0.1:8000/admin/')
            else:
                return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    auth.logout(request)
    return redirect('login')

def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(email__exact=request.user.email)
        success = user.check_password(current_password)
        if success:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password updated successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('change_password')
    return render(request, 'change_password.html')


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Reset password email

            current_site = get_current_site(request)
            message = render_to_string('ResetPassword_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            send_mail(
                'Please activate your account',
                message,
                'garbagemanagement3@gmail.com',
                [email],
                fail_silently=False,
            )

            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    return render(request, 'Forgot_Password.html')


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')


def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    else:
        return render(request, 'ResetPassword.html')




def payment_page(request):

    client = razorpay.Client(auth=("rzp_test_n7irR21xKIBPBj", "4DNQcF66EGnIWV2huNtZXz0Q"))

    DATA = {
        "amount": 500,
        "currency": "INR",
        "receipt": "receipt#1",

    }
    client.order.create(data=DATA)
    return render(request,"payment.html")


def payment_done(request):
    if request.session['email'] == 'null':
        return redirect('accounts/login')

    elif 'email' in request.session:
        email = request.session['email']
        public = Account.objects.get(email=email)
        messages.info(request, "successfully registered")
        public.status = 1
        public.save()
        return redirect('registration1.html')






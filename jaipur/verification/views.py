from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
import random
from .helper import MessageHandler

def home(request):
    if request.COOKIES.get('verified') and request.COOKIES.get('verified')!=None:
        return HttpResponse(" verified.")
    else:
        return HttpResponse(" Not verified.")
# from uuid import uuid4
# def register(request):
#     if request.method == "POST":
#         if User.objects.filter(username__iexact=request.POST['user_name']).exists():
#             return HttpResponse("User already exists")

#         user = User.objects.create(username=request.POST['user_name'])
#         otp = random.randint(1000, 9999)
#         profile = Profile.objects.create(user=user, phone_number=request.POST['phone_number'], otp=f'{otp}')
#         print(profile.uid)  # This should give you a valid UUID

#         if request.POST['methodOtp'] == "methodOtpWhatsapp":
#             messagehandler = MessageHandler(request.POST['phone_number'], otp).send_otp_via_whatsapp()
#         else:
#             messagehandler = MessageHandler(request.POST['phone_number'], otp).send_otp_via_message()
        
#         red = redirect('otp', user=profile.user)
        
#         red.set_cookie("can_otp_enter", True, max_age=600)
#         return red  
#     return render(request, 'register.html')

# from uuid import UUID
# from django.shortcuts import get_object_or_404

# def otpVerify(request, user):
#     print("otp verifying")
#     print("Received uid:",(user))
    
#     try:
#         # user = get_object_or_404(User, user=uid)
#         # # Fetch the profile associated with the user
#         #profile = get_object_or_404(Profile, user=user)
#         print("hhh")
#         profile = Profile.objects.filter(user=user)
#         #profile= Profile.objects.get(user=user)
         
#     except ValueError:
#         return HttpResponse(ValueError)
    
#     if request.method == "POST":
#         if request.COOKIES.get('can_otp_enter') is not None:
#             if profile.otp == request.POST['otp']:
#                 red = redirect("home")
#                 red.set_cookie('verified', True)
#                 return red
#             return HttpResponse("wrong otp")
#         return HttpResponse("10 minutes passed")        
#     return render(request, "otp.html", {'id': user})


def register(request):
    if request.method=="POST":
        if User.objects.filter(username__iexact=request.POST['user_name']).exists():
            return HttpResponse("User already exists")

        user=User.objects.create(username=request.POST['user_name'])
        otp=random.randint(1000,9999)
        profile=Profile.objects.create(user=user,phone_number=request.POST['phone_number'],otp=f'{otp}')
        if request.POST['methodOtp']=="methodOtpWhatsapp":
            messagehandler=MessageHandler(request.POST['phone_number'],otp).send_otp_via_whatsapp()
        else:
            messagehandler=MessageHandler(request.POST['phone_number'],otp).send_otp_via_message()
        red=redirect(f'otp/{profile.uid}/')
        red.set_cookie("can_otp_enter",True,max_age=600)
        return red  
    return render(request, 'register.html')

def otpVerify(request,uid):
    if request.method=="POST":
        profile=Profile.objects.get(uid=uid)     
        if request.COOKIES.get('can_otp_enter')!=None:
            if(profile.otp==request.POST['otp']):
                red=redirect("home")
                red.set_cookie('verified',True)
                return red
            return HttpResponse("wrong otp")
        return HttpResponse("10 minutes passed")        
    return render(request,"otp.html",{'id':uid})
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.template import loader
from datetime import datetime
from home.models import contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

# password for test user is chakkkkk$333

def index(request):
     
     # context={
     #      "a1":"Bipin",
     #      "a2":"Bipi",
     #      "a3":"Bip"
     # }
     if request.user.is_anonymous:
           return redirect("/login")
      
     messages.success(request,"You are Valid User")
      
     return render(request,'index.html')
     
     #template=loader.get_template('index.htm')
## return HttpResponse(template.render())

def loginuser(request):
     if request.method =="POST":
          username =request.POST.get('username')
          password=request.POST.get('password')
          # check if user has entered correct credentials
          user = authenticate(username=username, password=password)
          if user is not None:
               login(request,user)
               return redirect("/")
    # A backend authenticated the credentials
          else:
               return render(request,'login.html')
    # No backend authenticated the credentials
     return render(request,'login.html')

def signupuser(request):
     if request.method=="POST":
          username=request.POST.get('username')
          email=request.POST.get('email')
          password1=request.POST.get('password1')
          password2=request.POST.get('password2')
          user = User.objects.create_user(
    self.cleaned_data['username'],
    email=self.cleaned_data['email'],
    password1=self.cleaned_data['password1'],
    password2=self.cleaned_data['password2']
    
)
          user.save()
          return HttpResponse("User has been Created Successfully!")
          print(username,email,password1,password2)
          
          
     return render(request,'signup.html')

def logoutuser(request):
      logout(request)
      return redirect('/login')
 
def about(request):
     if request.user.is_anonymous:
           return redirect("/login")

     return render(request,'about.html')
     # return HttpResponse("This is about page")

def contactme(request):
     if request.user.is_anonymous:
           return redirect("/login")

     if request.method == "POST":
          fname = request.POST.get('fname')
          lname = request.POST.get('lname')
          username = request.POST.get('username')
          city = request.POST.get('city')
          message = request.POST.get('message')
          Contact =contact(fname=fname,lname=lname,username=username,city=city,message=message,date=datetime.today())
          Contact.save()
          messages.success(request, 'Your message has been sent !')
     return render(request,'contact.html')
     # return HttpResponse("This is service page")

def song(request):
     if request.user.is_anonymous:
           return redirect("/login")
     
     return render(request,'songs.html')#,context)
     # return HttpResponse("This is contact page")
# Create your views here.

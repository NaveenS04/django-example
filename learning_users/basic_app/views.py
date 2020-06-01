from django.shortcuts import render
from basic_app.forms import User,UserProfileInfodata


from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):

    return render(request,'basic_app/index.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == "POST":

        user_form = User(data=request.POST)
        pic_form = UserProfileInfodata(data=request.POST)

        if user_form.is_valid() and pic_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = pic_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:

                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,pic_form.errors)

    else:

        user_form = User()
        pic_form = UserProfileInfodata()

    return render(request,'basic_app/register.html',
                            {'user_form':user_form,
                             'pic_form':pic_form,
                             'registered':registered})

def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:

            if user.is_active:

                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:

                return HttpResponse("Your account is not active")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,"basic_app/login.html",{})

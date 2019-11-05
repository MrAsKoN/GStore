from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser
from django.shortcuts import get_object_or_404

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            emailId = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {username}!')
            send_mail(
                'Registration for Gstore',
                'Dear ' + username + ',' + '\n\n\tThank you for creating a Gstore account.\n\n Enjoy your new account,\nGstore Team',
                settings.EMAIL_HOST_USER,
                ['umang.prajapati1999@gmail.com', emailId],
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def editprofile(request):
    if request.method == 'POST':
        # userform = EditProfileForm(request.POST)
        # profileform = EditProfileForm(request.POST)
        # if userform.is_valid() and profileform.is_valid():
        #     user = userform.save()
        #     print(user)
        #     profile = profileform.save(commit=True)
        #     print(profile)
        #     profile.user = user
        #     print(request.FILES)
        #     if 'profile-avatar' in request.FILES:
        #         print(1212)
        #         profile.avatar=request.FILES['profile-avatar']
        #     profile.save()
        #     return redirect('profile')
        print('5467')
        userform = EditProfileForm(request.POST)
        print(userform)
        user_data = userform.data
        firstName = user_data['FirstName']
        print(firstName)
        lastName = user_data['LastName']
        address = user_data['address']
        phone = user_data['phoneno']
        #avatar = user_data['avatar']
        user_unq = get_object_or_404(CustomUser,user = request.user)
        user_unq.firstname = firstName
        user_unq.lastname = lastName
        user_unq.address = address
        #user_unq.avatar = avatar
        user_unq.phoneno = phone
        if 'avatar' in request.FILES:

            print(request.FILES['avatar'])
            user_unq.avatar = request.FILES['avatar']
        #print(avatar)
        #print(type(avatar))
        print(user_unq)
        user_unq.save()
        context = {
            'userform': user_unq
        }
        return redirect('profile')
    else:
        userform = EditProfileForm(request.POST)
        # avatar = user_data['avatar']
        user_unq = get_object_or_404(CustomUser, user=request.user)
        context = {
            'userform': user_unq

        }
        return render(request, 'users/editprofile.html', context)

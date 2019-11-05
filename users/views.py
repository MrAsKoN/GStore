from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


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
        userform = EditProfileForm(request.POST, instance=request.user, prefix='user')
        profileform = EditProfileForm(request.POST, instance=request.user.customuser, prefix="profile")
        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            print(user)
            profile = profileform.save(commit=True)
            print(profile)
            profile.user = user
            print(request.FILES)
            if 'profile-avatar' in request.FILES:
                print(1212)
                profile.avatar=request.FILES['profile-avatar']
            profile.save()
            return redirect('profile')
    else:
        userform = EditProfileForm(request.POST, instance=request.user, prefix='user')
        profileform = EditProfileForm(request.POST, instance=request.user.customuser, prefix="profile")
        context = {
            'userform': userform,
            'profileform': profileform
        }
        return render(request, 'users/editprofile.html', context)

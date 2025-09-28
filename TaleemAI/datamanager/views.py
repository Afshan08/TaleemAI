from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from datamanager.forms import SignupForm, LoginForm
from datamanager.models import UserProfile, MCQ


def home(request):
    return render(request, 'home.html', {
        'user': request.user
    })


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']
            UserProfile.objects.create(user=user, role=role)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')  # Assuming a home view exists; adjust as needed
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('home')  # Assuming a home view exists; adjust as needed
            else:
                messages.error(request, 'Invalid credentials.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')


def entry_test(request):
    if not request.user.is_authenticated:
        return redirect('login')
    questions = MCQ.objects.all()[:5]  # Fetch first 5 questions for the test
    return render(request, 'entry_test.html', {
        'user': request.user,
        "questions": questions
    })



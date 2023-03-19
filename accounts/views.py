from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.forms import CreateUserForm
from accounts.models import Room, Guest
# from accounts.models import Contact_us


def registerPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return render(request, 'login.html')
    return render(request, "register.html")


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def HomepageView(request):
    if not request.user.is_authenticated:
        return redirect('login.html')
    return render(request, 'index.html')


def rooms_list(request):
    data = Room.objects.all()

    return render(request, 'rooms_list.html', {"messages": data})


def roomView(request):
    if not request.user.is_authenticated:
        return redirect('login.html')
    return redirect('rooms_list.html')


def booking_list(request):
    data = Guest.objects.all()

    return render(request, 'booking_list.html', {"messages": data})


def bookView(request):
    if not request.user.is_authenticated:
        return redirect('login.html')
    return redirect('booking_list.html')


def book(request):
    return render(request, 'book.html')


def user_book(request):
    username = request.POST['user']
    Email = request.POST['email']
    Phone = request.POST['phone']
    Address = request.POST['address']
    City = request.POST['city']
    State = request.POST['state']
    room = request.POST['room']
    check_in = request.POST['check_in']
    check_out = request.POST['check_out']

    Guest(user=username, email=Email, phone=Phone, address=Address, city=City, state=State, room=room,
          Check_in=check_in, Check_out=check_out).save()

    return render(request, 'book.html')


def contact(request):
    #     Username = request.POST['user2']
    #     Email = request.POST['email']
    #     Phone = request.POST['phone']
    #
    #     Contact_us(user=Username, email=Email, phone=Phone).save()
    return render(request, 'contact.html')


def contactView(request):
    if not request.user.is_authenticated:
        return redirect('login.html')
    return redirect('contact.html')

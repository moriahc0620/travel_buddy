from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'first_app/index.html')

def register(request): # added session
    print request.POST
    result = User.objects.val_reg(request.POST)
    if result [0]:
        request.session['user_id'] = result[1].id
        request.session['username'] = result[1].username
        return redirect('/dashboard')
    else:
        for errors in result[1]:
            messages.add_message(request, messages.INFO, errors)
        return redirect('/')

def login(request): #added session
    result = User.objects.val_log(request.POST)
    if result [0]:
        request.session['user_id'] = result[1].id
        request.session['username'] = result[1].username
        return redirect('/dashboard')
    else:
        for error in result[1]:
            messages.add_message(request, messages.INFO, errors)
        return redirect('/')

def dashboard(request): # for the logged in user to add a trip in the add html page
    return render(request, 'first_app/dashboard.html')

def add(request):
    if 'id' not in request.session:
        return redirect ('/')
    else: context = {
        'user':User.objects.get(id=request.session['id']), 
    }
    return render(request, 'first_app/add.html', context)

def book(request): # for the logged in user to add a travel plan from their dashboard page using the link "add travel plan"
    if request.method != 'POST':
        return redirect('/add')
    book = Trip.objects.trip_val(request.POST, request.session["id"])
    if book[0] == True:
        return redirect('/destination')
    else:
        for message in book[1]:
            message.errors(request, message)
    return redirect('/add')

def join(request): # for the logged in user to click join from the dashboard from other user's travel plans
    return render(request, 'first_app/destination.html')

def logout(request): # deleting session for user to fully log out then redirects them to the index page
    if 'id' not in request.session:
        return redirect ('/')
    print request.session['id']
    del request.session['id'] 
    return redirect('/') 
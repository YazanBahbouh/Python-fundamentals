from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    return render(request, 'index.html')




def farm(request):
    if request.method == "POST":
        if not 'gold' in request.session:
            request.session['gold'] = random.randrange(10,20)
        else:
            request.session['gold'] += random.randrange(10,20)
        return redirect('/')
    else:
        return redirect('/')

def cave(request):
    if request.method == "POST":
        if not 'gold' in request.session:
            request.session['gold'] = random.randrange(5,10)
        else:
            request.session['gold'] += random.randrange(5,10)
        return redirect('/')
    else:
        return redirect('/')

def house(request):
    if request.method == "POST":
        if not 'gold' in request.session:
            request.session['gold'] = random.randrange(2,5)
        else:
            request.session['gold'] += random.randrange(2,5)
        return redirect('/')
    else:
        return redirect('/')

def casino(request):
    if request.method == "POST":
        if not 'gold' in request.session:
            request.session['gold'] = random.randrange(-50,50)
        else:
            request.session['gold'] += random.randrange(-50,50)
        return redirect('/')
    else:
        return redirect('/')


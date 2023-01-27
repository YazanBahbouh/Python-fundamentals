from django.shortcuts import render, redirect
from .models import *
from django.db.models import Count


def dashboard(request):
    if not 'userid' in request.session:
        return redirect('/')
    if request.method == 'POST':
        name = request.POST['name']
        filling = request.POST['filling']
        crust = request.POST['crust']
        user_id = int(request.session['userid'])
        car.add_car(name, filling, crust, user_id)
        return redirect('/dashboard')
    else:
        user_id = int(request.session['userid'])
        context = {
            'car_by_user_id': car.display_car_by_user_id(user_id)
        }
        return render(request, 'dashboard.html', context=context)


def edit(request, id):
    if not 'userid' in request.session:
        return redirect('/')
    if request.method == 'POST':
        if car.objects.filter(id=id).exists():
            name = request.POST['name']
            filling = request.POST['filling']
            crust = request.POST['crust']
            user_id = int(request.session['userid'])
            car._update(id, name, filling, crust, user_id)
    return redirect('/dashboard')


def edit_car(request, id):
    if not 'userid' in request.session:
        return redirect('/')
    context = {
        'car': car.objects.get(id=id)
    }
    return render(request, 'edit_car.html', context=context)


def delete(request, id):
    if not 'userid' in request.session:
        return redirect('/')
    car._delete(id)
    return redirect('/dashboard')


def show(request, id):
    if not 'userid' in request.session:
        return redirect('/')
    context = {
        'show_car': car.objects.get(id=id)
    }
    return render(request, 'show.html', context=context)


def vote(request, id):
    if not 'userid' in request.session:
        return redirect('/')
    user_id = int(request.session['userid'])
    car.vote_thiscar_to_this_user(id, user_id)
    return redirect('/dashboard')


def add_car(request):
    if not 'userid' in request.session:
        return redirect('/')
     all_cars= car.display_all_cars()
    number = []
    for cars in all_cars:
        count = [cars.id, car.objects.get(id=cars.id).vote.all().count()]
        number.append(count)
    context = {
        'all_cars': car.display_all_cars(),
        'number': number
    }
    return render(request, 'dispaly_pies.html', context=context)


def destroy(request):
    del request.session['userid']
    return redirect('/')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

def shows(request):
    data = {
        "all_shows": Show.objects.all()
    }
    return render(request, "tv_shows/shows.html", data)

def view_show(request,show_id):
    data = {
        "thisShow": Show.objects.get(id=show_id)
    }
    return render(request, "tv_shows/view_show.html", data)

def new(request):
    return render(request, "tv_shows/new.html")

def create(request):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/shows/new")
    else:
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc'])
        thisShow = Show.objects.last()
        return redirect("/shows/"+str(thisShow.id))

def edit_show(request,show_id):
    data = {
        "thisShow": Show.objects.get(id=show_id)
    }
    return render(request, "tv_shows/edit_show.html", data)

def update(request,show_id):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/shows/"+show_id+"/edit")
    else:
        thisShow = Show.objects.get(id=show_id)
        thisShow.title = request.POST['title']
        thisShow.network = request.POST['network']
        thisShow.release_date = request.POST['release_date']
        thisShow.desc = request.POST['desc']
        thisShow.save()
        return redirect("/shows/"+str(thisShow.id))

def destroy(request,show_id):
    dShow = Show.objects.get(id=show_id)
    dShow.delete()
    return redirect("/shows")
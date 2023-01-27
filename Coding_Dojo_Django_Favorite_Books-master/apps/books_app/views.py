from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
 
 
 
# Create your views here. 
def index(request): 

    allBooks = Book.objects.all
    thisUser = User.objects.get(id=request.session['cur_user'])

    context = {
        "allBooks" : allBooks,
        "user" : thisUser,
    }

    return render(request, 'books_app/index.html', context) 

def createBook(request):
    thisUser = User.objects.get(id=request.session['cur_user'])
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/books/')
    else:
        thisBook = Book.objects.new_book(request.POST, thisUser)
        thisBook.users_who_like.add(thisUser)
        return redirect('/books/')

def favoriteThisBook(request, id):
    thisBook = Book.objects.get(id=id)
    thisUser = User.objects.get(id=request.session['cur_user'])

    thisBook.users_who_like.add(thisUser)
    return redirect('/books/' + str(id))


def unFavoriteThisBook(request, id):
    thisBook = Book.objects.get(id=id)
    thisUser = User.objects.get(id=request.session['cur_user'])

    thisBook.users_who_like.remove(thisUser)
    return redirect('/books/' + str(id))

def updateBookDesc(request, id):
    thisBook = Book.objects.get(id=id)

    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/books/' + str(id))
    else:
        thisBook.desc = request.POST['desc']
        thisBook.save()

    return redirect('/books/' + str(id))

def thisBook(request, id):
    thisBook = Book.objects.get(id=id)
    thisUser = User.objects.get(id=request.session['cur_user'])

    context = {
        "book" : thisBook,
        "thisUser" : thisUser,

    }
    return render(request, 'books_app/book.html', context)

def deleteBook(request, id):
    thisBook = Book.objects.get(id=id)
    thisUser = User.objects.get(id=request.session['cur_user'])

    if thisBook.uploader == thisUser:
        thisBook.delete()

    return redirect('/books/')

def destroy(request):
    request.session.flush()
    return redirect('/')




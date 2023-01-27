import bcrypt
from django.db import models
from datetime import datetime


class usersManger(models.Manager):
    def basic_validtor(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 3:
            errors["first_name"] = "First name should be at least 3 characters"
        if len(post_data['last_name']) < 2:
            errors["last_name"] = "alias should be at least 3 characters"
        if len(post_data['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if post_data['password'] != post_data['confirm_password']:
            errors["confirm_password"] = "No match password "
        if User.objects.filter(email=post_data['email']).exists():
            errors["email"] = "Already existsed !!!!"
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = usersManger()


def Register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    if (request.POST['confirm_password'] == password):
        return User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)

def Login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        loged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), loged_user.password.encode()):
            request.session['userid'] = loged_user.id
            request.session['username']=loged_user.first_name
            return True
        else :
            request.session['LoginAuth'] = "Username or password does not exist"
            return False
    else:
        request.session['LoginAuth'] = "Username or password does not exist"
        return False
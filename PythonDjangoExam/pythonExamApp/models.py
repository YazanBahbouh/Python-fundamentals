from django.db import models
from loginAndRegisterApp.models import *


class car(models.Model):
    name = models.CharField(null=False, max_length=45)
    user = models.ForeignKey(User, related_name='car_user', on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True)

    def display_all_cars():
        return car.objects.all()

    def add_car(name, filling, crust, user_id):
        user_obj = User.objects.get(id=user_id)
        car.objects.create(name=name, filling=filling,
                             crust=crust, user=user_obj)

    def display_car_by_user_id(id):
        return car.objects.filter(user=id)

    def _update(id, name, filling, crust, user):
        _car = car.objects.get(id=id)
        user = User.objects.get(id=user)
        _car.name = name

        _car.user = user
        _car.save()

    def _delete(id):
        _car=car.objects.get(id=id)
        _car.delete()

from django.urls import path
from . import views


app_name = 'FinalExamApp'

urlpatterns =[
    path('',views.dashboard,name='dashboard'),
    path('edit/<int:id>',views.edit_car,name='edit_car'),
    path('car',views.add_pies,name='add_pies'),
    path('delete/<int:id>',views.delete,name='delete'),
]
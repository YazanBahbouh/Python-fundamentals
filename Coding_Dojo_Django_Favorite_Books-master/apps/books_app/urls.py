from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index), 
    path('destroy/', views.destroy), 
    path('create/', views.createBook), 
    path('desc/update/<int:id>', views.updateBookDesc), 
    path('<int:id>/', views.thisBook), 
    path('delete/<int:id>/', views.deleteBook), 
    path('favorite/<int:id>/', views.favoriteThisBook), 
    path('unfavorite/<int:id>/', views.unFavoriteThisBook), 

] 

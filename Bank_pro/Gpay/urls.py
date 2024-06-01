from django.urls import path
from . import views


urlpatterns = [
   
    path('',views.read),
    path('add/',views.add, name = 'add'),
    path('edit/',views.edit, name = 'edit'),
    path('update/<str:id>',views.update, name = 'update'),
    path('delete/<str:id>',views.delete, name = 'delete'),
    path('delete_all/',views.delete_all, name = 'delete_all'),


]
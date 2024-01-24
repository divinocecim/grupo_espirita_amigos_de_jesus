from django.urls import path
from . import views

urlpatterns = [
 path('enviapedido/', views.enviapedido, name='enviapedido'),

]
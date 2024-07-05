from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('items/', views.items),
    path('items/<int:id>', views.items),
#    path('/suppliers', views.suppliers),
 #   path('/locations', views.locations),
  #  path('/orders', views.orders),
    path('login/', views.login),
]

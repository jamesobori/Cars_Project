from django.urls import  path
from.import views
urlpatterns = [
    path('', views.cars_list, name='car_list'), 
    path('contact/', views.contact, name='contact'), 
    path('book/<int:pk>/', views.cars_detail, name='car_detail'),
]


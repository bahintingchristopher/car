from django.urls import path
from .import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('inventory/', views.inventory, name='inventory'),
#     path('contact/', views.contact, name='contact'),
# ]

urlpatterns = [
    path("", views.home, name="home"),
    path("inventory/", views.inventory, name="inventory"),
    path("contact/", views.contact, name="contact"),
    path("thankyou/", views.thankyou, name="thankyou"),

]

# urlpatterns = [
#     path('', views.inventory, name='inventory'),
# ]
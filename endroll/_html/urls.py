from django.urls import path

from . import views
urlpatterns = [
    path('home', views.index),
    # path('reserve/<int:pk>/', views.reserve)
    # path('disc/', views.disc_page)
    path('schedule', views.schedule),
    path('disc', views.disc),
    path('movie', views.movie),
    path('contact', views.contact)
]

from .views import profile,userpro
from django.urls import path,include


urlpatterns = [
    path('ser',profile.as_view()),
    path('ser/<str:key>',userpro.as_view())
]
from .views import *
from django.urls import path



urlpatterns = [
    path('',homepage),
    path('find',find),
    path('dbitemdisp',dbitemdisp),
    path('pro/<str:key>',details),
    path('addcart',addtocart),
    path('shopingcart',shopingcart),
    path('alldata',getalldata),
    path('search',search),
    path('produ/<str:keyw>',getproduct),
    

    
    
]
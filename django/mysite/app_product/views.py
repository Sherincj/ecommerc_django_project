from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# Create your views here.


def home(req):
    return render(req,'product.html',)
    


from .models import userinfo
def userdata(req):
    user= userinfo(name=req.POST['na'],
                   email=req.POST['em'],
                   password=req.POST['ps'],
                   phone=req.POST['ph'])

    user.save()
    return HttpResponse('user info created')

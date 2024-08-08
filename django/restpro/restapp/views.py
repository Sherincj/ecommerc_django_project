from django.shortcuts import render
from rest_framework.decorators import APIView
from .models import userprofile
from .serializers import userserializers
from rest_framework.response import Response
# Create your views here.


class profile(APIView):
    def get(self,request):
        profiles=userprofile.objects.all()
        newdata=userserializers(profiles,many=True)
        return Response(newdata.data)
    


    def post(self,request):
        newda=userserializers(data=request.data)
        if newda.is_valid():
            newda.save()
            return Response(newda.data)
        else:
            return Response('data not valid')
    


class userpro(APIView):
    def get(self,request,key):
        profile=userprofile.objects.get(id=key)
        newdata=userserializers(profile)
        return Response(newdata.data)
    

    def put(self,request,key):
        profile=userprofile.objects.get(id=key)
        newda=userserializers(profile,request.data)
        if newda.is_valid():
            newda.save()
            return Response(newda.data)
        else:
            return Response('data not valid')
        

    def delete(self,request,key):
        profile=userprofile.objects.get(id=key)
        profile.delete()
        return Response('user deleted')

    


    
    

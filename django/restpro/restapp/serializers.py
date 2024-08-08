from rest_framework.serializers import ModelSerializer
from .models import userprofile



class userserializers(ModelSerializer):
    class Meta:
        model= userprofile
        fields= '__all__'


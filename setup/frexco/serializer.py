from rest_framework import serializers
from .models import region, fruit




class regionSerializer(serializers.ModelSerializer):
    class Meta:
        model = region
        fields = ['Name']



class fruitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = fruit
        fields =['Name','regfruit']        


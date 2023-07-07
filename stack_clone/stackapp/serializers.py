from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Question,Answer

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
    def create(self, validated_data):
        return User.objects.create_user(validated_data)
    

class Questser(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    class Meta:
        model=Question
        fields="__all__"
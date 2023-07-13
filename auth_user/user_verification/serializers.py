from rest_framework import serializers
from . models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email','password')
        extra_kwargs = {'password':{'write_only':True}}



class OTPSerializer(serializers.ModelSerializer):
    class Meat:
        model = OTP
        fields = ('user','otp_code','timestamp')
                
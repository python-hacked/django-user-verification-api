from django.shortcuts import render
import random
from datetime import datetime,timedelta
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import *
from . serializers import CustomUserSerializer,OTPSerializer
# Create your views here.


@api_view(['POST'])
def create_user(request):
    serializer = CustomUserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        otp_code = str(random.randint(100000,999999))
        expiration_time = datetime.now() + timedelta(minutes=3)
        OTP.objects.create(user = serializer.instance,otp_code = otp_code, timestamp = expiration_time)
        # Simulate sending email with the OTP (print it for now)
        print(f"OTP for {serializer.instance.email}: {otp_code}")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

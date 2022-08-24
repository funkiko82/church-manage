# church/views.py
from django.shortcuts import render
# third party library
from rest_framework import generics
# local defined class
from .serializers import MemberListSerializer, MemberDetailSerializer

from .models import Member
# Create your views here.
# 
class MemberListAPIView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberListSerializer

class MemberRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Member.objects.all()
    serializer_class = MemberDetailSerializer

class MemberCreateAPIView(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberDetailSerializer

class MemberRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Member.objects.all()
    serializer_class =MemberDetailSerializer

class MemberDestroyAPIView(generics.DestroyAPIView):
   lookup_field = 'id'
   queryset = Member.objects.all()
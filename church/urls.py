# write your local url here
# church/urls.py

from django.urls import path

from . import views

urlpatterns = [path('', views.MemberListAPIView.as_view(), 
                    name='member_list'),
               path('<int:id>/', views.MemberRetrieveAPIView.as_view(),  
                    name='member_detail'), 
               path('create/', views.MemberCreateAPIView.as_view(), 
                    name='member_create'), 
               path('update/<int:id>/', 
                    views.MemberRetrieveUpdateAPIView.as_view(), name='member_update'), 
               path('delete/<int:id>/', views.MemberDestroyAPIView.as_view(), 
                    name='member_delete'),]
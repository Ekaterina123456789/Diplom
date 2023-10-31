from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('blogs/<str:pk>/', views.blog, name='blog'),
    path('create-blog/', views.create_blog, name='create-blog'),

]
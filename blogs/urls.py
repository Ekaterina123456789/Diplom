from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('blogs/<str:pk>/', views.blog, name='blog'),
    path('create-blog/', views.create_blog, name='create-blog'),
    path('update-blog/<str:pk>/', views.update_blog, name='update-blog'),

    path('update-advertisement/<str:pk>/', views.update_advertisement, name='update-advertisement'),
    path('about', views.about, name='about'),
]

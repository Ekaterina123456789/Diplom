from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.user_profile, name='user_profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('account/', views.user_account, name='account'),
    path('edit-account/', views.edit_account, name='edit-account'),

    path('create-skill/', views.create_skill, name='create-skill'),
    path('delete-skill/<int:pk>/', views.delete_skill, name='delete-skill'),
    path('update-skill/<int:pk>/', views.update_skill, name='update-skill'),

    path('inbox/', views.inbox, name='inbox'),
    path('message/<pk>', views.view_message, name='message'),
    path('create-message/<profile_pk>', views.create_message, name='create-message'),
    # path('answer-message/<int:pk>', views.answer_message, name='answer-message'),
]

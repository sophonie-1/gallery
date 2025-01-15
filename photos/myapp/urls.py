from django.urls import path
from .views import gallery, viewphoto, addphoto,list_photo_with_associated_category,login_view,register_view,logout_view,abantu




urlpatterns = [
    path('', gallery, name='gallery'),
    path('viewphoto/<str:pk>/', viewphoto, name='viewphoto'),
    path('addphoto/', addphoto, name='addphoto'),
    path('category/<str:pk>/', list_photo_with_associated_category, name='list_photo'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('abantu/', abantu, name='abantu')
]
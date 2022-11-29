from django.urls import path
from app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.uploadImage, name="upload"),
    path("delete/<int:id>", views.delete_image, name="delete"),
    path("signup/", views.user_signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]

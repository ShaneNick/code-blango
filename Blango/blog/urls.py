from django.urls import path
from . import views

urlpatterns = [
    path('blog/post', views.show_post)
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jocelyn", views.jocelyn, name="jocelyn"),
    path("<str:name>", views.greet, name="greet"),
]

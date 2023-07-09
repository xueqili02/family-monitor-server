from django.urls import path

from . import views

urlpatterns = [
    path("object_recognition/", views.object_recognition, name="object_recognition"),
    path("camera/", views.camera, name="camera"),
    path("range_coordinate/", views.range_coordinate, name="range_coordinate"),
]
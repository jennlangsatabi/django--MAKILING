from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("jenn", views.jenn, name="jenn"),
    path("britnie", views.britnie, name="Britnie")
]
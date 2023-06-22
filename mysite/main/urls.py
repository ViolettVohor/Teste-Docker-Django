from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("<int:id>", views.lista, name="lista"),
    path("create/", views.create, name="create"),
    path("lists/", views.lists, name="lists"),
]

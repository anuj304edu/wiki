from django.urls import path
import re
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.s_entry, name="s_entry"),
    path("search/", views.search, name="search"),
    path("createnewpage/", views.createnewpage, name="createnewpage"),
    path("editpage/<str:title>", views.editpage, name="editpage"),
    path("deletepage/<str:title>", views.deletepage, name="deletepage"),
    path("random/", views.randompage, name="randompage"),
]

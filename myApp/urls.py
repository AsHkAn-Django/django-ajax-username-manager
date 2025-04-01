from django.urls import path
from . import views

urlpatterns = [
    path("get-data/", views.get_data, name="get_data"),
    path("get-csrf-token/", views.get_csrf_token, name="get_csrf_token"),
    path("get-saved-names/", views.get_saved_names, name="get_saved_names"),
    path('delete-name/', views.delete_name, name='delete_name'),
    path('edit-name/', views.edit_name, name='edit_name'),
    path('', views.home, name='home'),
]

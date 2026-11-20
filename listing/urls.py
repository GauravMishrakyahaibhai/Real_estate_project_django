from django.urls import path
from . import views

urlpatterns = [
    path("", views.property_list, name="property_list"),
    path("property/<int:id>/", views.property_detail, name="property_detail"),
    path("add/", views.add_property, name="add_property"),
    path("update/<int:id>/", views.update_property, name="update_property"),
    path("delete/<int:id>/", views.delete_property, name="delete_property"),
]
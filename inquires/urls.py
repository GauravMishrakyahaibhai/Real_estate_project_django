from django.urls import path
from . import views

urlpatterns = [
    path("", views.inquiries, name="inquiries"),
    path("send/<int:property_id>/", views.send_inquiry, name="send_inquiry"),
]
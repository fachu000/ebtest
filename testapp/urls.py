from django.contrib import admin
from django.urls import path
from testapp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('home/', TemplateView.as_view(template_name="testapp/index.html"))
]

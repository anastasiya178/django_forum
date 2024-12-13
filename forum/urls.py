from django.urls import path
from . import views

# template tagging

app_name = 'forum'

urlpatterns = [
    # dashboard
    path('', views.get_dashboard, name='dashboard'),
    ]
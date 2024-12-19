from django.urls import path
from . import views

# template tagging

app_name = 'forum'

urlpatterns = [
    # dashboard
    path('', views.get_dashboard, name='dashboard'),
    path('categories/', views.CategoryList.as_view(), name="category_list"),
    path('categories/<int:c_pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
]

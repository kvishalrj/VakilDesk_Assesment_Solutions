from django.urls import path
from .views import top_customers_view, home_view

urlpatterns = [
    path('', home_view, name='home'), 
    path('top-customers/', top_customers_view, name='top_customers'),
]

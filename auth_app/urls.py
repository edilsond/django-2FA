from django.urls import path, include
from two_factor.urls import urlpatterns as two_factor_urls

urlpatterns = [
    path('', include(two_factor_urls)),
]
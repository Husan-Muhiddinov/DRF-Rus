from django.urls import path
from .views import WomenAPIView, WomenAPIList

  
urlpatterns = [
    path('api/v1/womenlist/', WomenAPIList.as_view(), name='women'),
    path('api/v1/womenlist/<int:pk>/', WomenAPIList.as_view(), name='womenn'),
]
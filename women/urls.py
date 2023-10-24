from django.urls import path
from .views import WomenAPIView, WomenAPIList, WomenAPIUpdate, WomenAPIDetailView, WomenViewSet
from rest_framework import routers




router = routers.SimpleRouter()
router.register(r'api/v1/women/', WomenViewSet)
  
urlpatterns = [
    
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get':'list'}), name='women'),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet .as_view({'put':'update'}), name='womenn'),

    # path('api/v1/womenlist/', WomenAPIList.as_view(), name='women'),
    # path('api/v1/womenlist/<int:pk>/', WomenAPIUpdate .as_view(), name='womenn'),
    # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView .as_view()),
]

urlpatterns += router.urls
from django.urls import path
from .views import WomenAPIView, WomenAPIList, WomenAPIUpdate, WomenAPIDetailView, WomenViewSet
from rest_framework import routers


class MyCustomRouter(routers.SimpleRouter):
    
    routes = [
        routers.Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
                'post': 'create'
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        routers.Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Instance'}
        ),
    ]



router = MyCustomRouter()
router.register(r'api/v1/women/', WomenViewSet, basename='women')
  
urlpatterns = [
    
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get':'list'}), name='women'),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet .as_view({'put':'update'}), name='womenn'),

    # path('api/v1/womenlist/', WomenAPIList.as_view(), name='women'),
    # path('api/v1/womenlist/<int:pk>/', WomenAPIUpdate .as_view(), name='womenn'),
    # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView .as_view()),
]

urlpatterns += router.urls
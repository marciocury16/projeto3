from django.contrib import admin
from django.urls import path, include
from frexco.views import regionViewSet, fruitViewSet
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from frexco import views


router = routers.DefaultRouter()
router.register(r'regiao',regionViewSet)
router.register(r'fruta',fruitViewSet)

urlpatterns = format_suffix_patterns

urlpatterns = [
    path('snippets/', views.fruit),
    path('snippets/<int:pk>/', views.fruitDetail.as_view()), 
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    

]




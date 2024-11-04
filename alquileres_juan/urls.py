"""
URL configuration for alquileres_juan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from alquiler import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicle/<int:pk>/detail',views.VehicleDetail.as_view(),name='vehicle_detail'),
    path('vehicle/add',views.VehicleAdd.as_view(),name='vehicle_form'),
    path('vehicle/list',views.VehicleList.as_view(),name='vehicle_list'),
    path('vehicle/<int:pk>/update',views.VehicleUpdate.as_view(),name='vehicle_update'),
    path('vehicle/<int:pk>/delete',views.VehicleDelete.as_view(),name='vehicle_delete'),
    path('user/add',views.UserAdd.as_view(),name='user_form'),
    path('user/list',views.UserList.as_view(),name='user_list'),
    path('user/<int:pk>/delete',views.UserDelete.as_view(),name='user_delete'),
    path('user/<int:pk>/update',views.UserUpdate.as_view(),name='user_update'),

]


from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('',include('sample.urls')),
    path('api/',include('api.urls')),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path
from .views import DecodeTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('decode', DecodeTokenView.as_view(), name='decode-token')
]

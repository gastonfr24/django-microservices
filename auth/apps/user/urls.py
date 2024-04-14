from django.urls import path
from .views import DecodeTokenView

urlpatterns = [
    path('decode', DecodeTokenView.as_view(), name='decode-token')
]

from django.urls import re_path as url
from django.urls import path, include
from .views import (
    TestModelListApiView,
    TestModelDetailApiView
)

urlpatterns = [
    path('api/', TestModelListApiView.as_view()),
    path('api/<int:testmodel_id>/', TestModelDetailApiView.as_view())
]


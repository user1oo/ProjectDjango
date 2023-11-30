
from django.urls import path
from property_web.views import index

urlpatterns = [
    path("list/", index)
]

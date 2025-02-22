from django.urls import path
from .views import blackscholes


urlpatterns = [
    path('', blackscholes, name="blackscholes-index"),
]
from django.urls import path
from .views import SignUp, SignUp01

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
]
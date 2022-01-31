import imp
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users_api import views

urlpatterns = [
    path('signup/',views.signup.as_view()),
    path('login/',views.login.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
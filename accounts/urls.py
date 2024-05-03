from django.urls import path
from .views.signin import Signin
from .views.signup import Signup
from .views.user import GetUser

urlpatterns = [
    path('signin', Signin.as_view()),
    path('signup', Signup.as_view()),
    path('user', GetUser.as_view()),
]

class FixView:
    template_name = 'user/user_form.html'
    next_page = 'user_login'


# ----------------------------
# User Login/Logout
# ----------------------------
from django.contrib.auth.views import LoginView, LogoutView


class UserLoginView(FixView, LoginView):
    pass


class UserLogoutView(FixView, LogoutView):
    pass


# ----------------------------
# User Registration
# ----------------------------
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

class UserCreateView(FixView, CreateView):
    form_class = UserCreationForm
REDIRECT_URL_PATHNAME = 'user_login'

class FixView:
    template_name = 'user/user_form.html'
    next_page = REDIRECT_URL_PATHNAME


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
# from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class UserCreateView(FixView, CreateView):
    form_class = UserCreationForm
    # success_url = '/user/login/'
    success_url = reverse_lazy(REDIRECT_URL_PATHNAME)

    # Login after registration:
    def get_success_url(self):
        from django.contrib.auth import login
        login(self.request, self.object)
        return super().get_success_url()
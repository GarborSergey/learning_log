"""Определяет схемы url для пользователей"""

from django.urls import path, include  # for login page
from . import views   # for registration page
from django.contrib.auth import login

app_name = 'users'
urlpatterns = [
    # Для входа пользователя в систему из представления используйте login().
    # Он принимает HttpRequestпредмет и Userпредмет.
    # login()сохраняет идентификатор пользователя в сеансе, используя структуру сеанса Django.
    # login() представление django по умолчанию
    path('login/', login, {'template_name': 'users/login.html'}, name='login')
]

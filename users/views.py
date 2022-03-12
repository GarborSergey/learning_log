
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# Проще всего воспользоваться UserCreationForm и представлением на основе класса CreateView,
# предоставляемыми Django.
# UserCreationForm - это класс ModelForm для создания нового пользователя, который генерирует требуемые поля,
# а именно username и password.
from django.views.generic.edit import CreateView




# Добавляю класс представления

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
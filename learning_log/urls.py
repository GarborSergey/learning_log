# Ипорт функций и модулей, управляющие URL адресами проекта и административным сайтом

from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    # Функция include() позволяет ссылаться на другие URLconfs.
    # Всякий раз, когда Django встречает include(), он отсекает любую часть URL-адреса,
    # совпадающую с этой точкой, и отправляет оставшуюся строку во включенный URLconf для дальнейшей обработки.
    # первая чать выражения это url после адреса сайта
    path('', include('learning_logs.urls', namespace='learning_logs')),  # namespace не работает без app_name в urls приложения
    path('admin/', admin.site.urls)

]

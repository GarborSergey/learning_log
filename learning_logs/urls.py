"""Определяет схемы URL для learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со всеми темаи
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>', views.topic, name='topic'),  #<int:post_id>
    # Страница с добовлением новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница с добовлением новой записи к теме
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Страница с редактированием записей
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Страница с инфой
    path('info/', views.take_info, name='take_info')
]

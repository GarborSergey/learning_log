from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # CASCADE так как внешний ключ требует 2 обяз, аргумента


    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text

class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    # Внешний ключ, содержит ссылку на другую запись в базе данных, таким образом каждая запись связывается с определенной темой
    # Позволяет реализовать один от многих
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # CASCADE так как внешний ключ требует 2 обяз, аргумента
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # Класс мета хранит дополнительную информацию по управлению моделью
    # позволяет задать специальный атрибут который приказывает django использовать
    # форму множественного числа Entries при обращении более чем к одной записи
    class Meta:
        verbose_name_plural = 'entries'


    # Сообщает какая информация должна отоброжаться при обращении к отдельным записям
    def __str__(self):
        """Возвращает сроковое представление модели"""
        if len(self.text) <= 50:
            return self.text
        else:
            return self.text[:50] + '...'


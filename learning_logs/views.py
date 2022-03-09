# Представления сайта
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Topic, Entry
from django.urls import reverse
from .forms import TopicForm, EntryForm


def index(request):
    """Домашняя страница приложения learning log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Выводит список тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Выводит одну тему и все ее записи"""
    topic = Topic.objects.get(id=topic_id)
    # запрос 1 к БД
    entries = topic.entry_set.order_by('-date_added')  # - сортирует записи в обратном порядке
    # запрос 2 к БД
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Определяет новую тему"""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма
        form = TopicForm()
    else:
        # Отправленны данные POST; обработать данные
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context ={'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Добавляет новую запись по конкретной теме"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма
        form = EntryForm()
    else:
        # Отправленны данные POST; обработать данные
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """Редактирует существующую запись"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи
        form = EntryForm(instance=entry)
    else:
        # отправка данных POST; обработать данные
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
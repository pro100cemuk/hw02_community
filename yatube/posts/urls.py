from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница со постами, отфильтрованными по группам
    path('group/<slug>/', views.group_posts, name='group_list'),
]

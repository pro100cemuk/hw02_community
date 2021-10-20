"""yatube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# По умолчанию в проект Django подключена система администрирования
from django.contrib import admin
# Функция include позволит использовать path() из других файлов.
from django.urls import include, path

urlpatterns = [
    # Дорогой Джанго, если запрошена главная страница (''),
    # перейди в файл urls приложения posts и проверь там все пути
    path('', include('posts.urls')),
    # Встроенная админка в Django подключена по этому адресу «из коробки»
    path('admin/', admin.site.urls),
]

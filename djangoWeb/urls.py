"""
URL configuration for djangoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.http import HttpResponseNotFound
from django.urls import path, include, re_path, register_converter
from games import views
from games import converters
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница ненайдена</h1>')
handler404 = page_not_found
register_converter(converters.FourDigitYearConverter, "year4")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('archive/<year4:year>/', views.archive),
    path('', include('games.urls')),
]

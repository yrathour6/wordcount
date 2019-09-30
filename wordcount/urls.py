from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index,name='index'),
    path('about', view.about,name='about'),
    path('about', view.about1,name='about1'),
]

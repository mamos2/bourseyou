from django.urls import include, path

from . import views

urlpatterns = [
    # ex: /polls/
    path (r'^$', views.index, name='index'),

]

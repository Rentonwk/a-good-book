from django.conf.urls import url
from gdbook import views

urlpatterns = [
    url(r'^main/$', views.home, name='index'),
]
from .views import testview

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'test/$', testview, name='test')
]
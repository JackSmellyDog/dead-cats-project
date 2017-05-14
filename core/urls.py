from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='base'),
    url(r'^search', TemplateView.as_view(template_name="search.html"), name='search'),
    url(r'^success', TemplateView.as_view(template_name="success.html"), name='success'),
]

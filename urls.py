from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import IndexView

app_name = 'news'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^search$', views.search, name='search'),
   # url(r'^(?P<location_name>(.*)+)/$', views.detail, name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
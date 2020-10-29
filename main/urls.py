from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('kitchen', views.kitchen, name='kitchen'),
    path('craft_beer', views.craft_beer, name='craft_beer'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('farmhouse_ale', views.farmhouse_ale, name='farmhouse_ale'),
    path('bavarian_weizen', views.bavarian_weizen, name='bavarian_weizen'),
    path('dark_lager', views.dark_lager, name='dark_lager'),
    path('apa', views.apa, name='apa'),
    path('ipa', views.ipa, name='ipa'),
    path('cherry_ale', views.cherry_ale, name='cherry_ale'),
    path('apple_cider', views.apple_cider, name='apple_cider'),
    path('dipa', views.dipa, name='dipa'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

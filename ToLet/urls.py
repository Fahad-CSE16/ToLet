
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from buildings.views import FlatList
urlpatterns = [
    path('admin/', admin.site.urls),
    path('acc/', include('accounts.urls')),
    path('flat/', include('buildings.urls')),
    path('serve/', include('services.urls')),
    path('',FlatList.as_view(), name='home'),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


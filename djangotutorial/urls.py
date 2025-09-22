from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('key/', home , name='home'), 
    path('jump/', include ('cars.urls')),
    path('burn/', include ('colour.urls')),
    path('red/', include ('colour.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
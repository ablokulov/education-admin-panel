
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('app.users.urls')),
    path('api/',include('app.teacher.urls')),
    path('api/',include('app.groups.urls')),
    path('api/',include('app.students.urls')),
    path('api/',include('app.notifications.urls')),
    


    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


if settings.DJANGO_ENV == 'development':
    from debug_toolbar.toolbar import debug_toolbar_urls
    from django.conf.urls.static import static
    
    
    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    
    

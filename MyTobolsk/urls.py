from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path
from rest_framework import routers

from events.views import EventsViewSet
from routes.views import RoutesViewSet
from stories.views import StoriesViewSet
from users.views import UsersViewSet

router = routers.DefaultRouter()
router.register(r'events', EventsViewSet)
router.register(r'routes', RoutesViewSet)
router.register(r'stories', StoriesViewSet)

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

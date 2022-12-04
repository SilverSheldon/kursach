from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from api import views
from kyrsovaya import settings
from myapp1.views import index_page
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name = "functional"),
    path('api/<str:s>', views.StatisticsView.as_view(), name="statistics"),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

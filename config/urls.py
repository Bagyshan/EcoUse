from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="EcoUse",
        description="mini service for posting your life",
        default_version="v1",
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('jazzmin/', include('jazzmin.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('account/', include('account.urls')),
    path('category/', include('category.urls')),
    path('products/',include('product.urls')),
    path('home/', include('home.urls')),
    path('recommendation/', include('recommendation.urls')),
    path('parent_category/', include('parent_category.urls'))
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
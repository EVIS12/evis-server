from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

api_prefix = "api/v1/"

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
    path(f"{api_prefix}auth/", include("djoser.urls.jwt")),
]

# Accounts
urlpatterns += [
    path(f"{api_prefix}accounts/", include("evis.accounts.api.urls")),
    path(f"{api_prefix}advisors/", include("evis.speakers.advisors.urls")),
    path(f"{api_prefix}analysis/", include("evis.dashboard.analysis.urls")),
    path(f"{api_prefix}blog/", include("evis.blog.urls")),
    path(f"{api_prefix}conference/", include("evis.conference.urls")),
    path(f"{api_prefix}dashboard/", include("evis.dashboard.urls")),
    path(f"{api_prefix}exhibitor/", include("evis.exhibitor.urls")),
    path(f"{api_prefix}home/", include("evis.home.urls")),
    path(f"{api_prefix}links/", include("evis.users.urls")),
    path(f"{api_prefix}speakers/", include("evis.speakers.urls")),
    path(f"{api_prefix}visit/", include("evis.visit.urls")),
    path(f"{api_prefix}interest/", include("evis.visit.api.urls")),
]
if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

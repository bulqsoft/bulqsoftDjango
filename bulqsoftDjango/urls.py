from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
import django.views.i18n
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns  # Make sure this is included

# Django's i18n views must be explicitly included for the language switching functionality
from django.conf.urls import url

admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    url(r'^setlang',  django.views.i18n.set_language, name="set_language"),
]

# Add i18n URL patterns (this should already be included)
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("cms.urls")),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

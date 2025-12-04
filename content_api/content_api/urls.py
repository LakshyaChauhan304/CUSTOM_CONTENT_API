from django.contrib import admin
from django.urls import path, include, re_path
from CONTENT_APP.views import home,signup

# Wagtail imports
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

# Wagtail API Router
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.views import PagesAPIViewSet

api_router = WagtailAPIRouter('wagtailapi')
api_router.register_endpoint('pages', PagesAPIViewSet)

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('content/', include('CONTENT_APP.urls')),   # all app routes
    path('admin/', include(wagtailadmin_urls)),      # Wagtail admin
    path('documents/', include(wagtaildocs_urls)),
    path('api/v2/', api_router.urls),
                 # Wagtail front-end pages

    path('', home,name='home'),
    path('signup/',signup,name="signup"),
    
    
    re_path(r'', include(wagtail_urls)),
]

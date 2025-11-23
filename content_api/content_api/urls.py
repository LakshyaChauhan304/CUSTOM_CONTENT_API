"""
URL configuration for content_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.views import PagesAPIViewSet

api_router = WagtailAPIRouter('wagtailapi')
api_router.register_endpoint('pages', PagesAPIViewSet)

urlpatterns = [
   # Django admin
    path("admin/", admin.site.urls),

    # Wagtail admin
    path("cms/", include("wagtail.admin.urls")),

    # Wagtail documents
    path("documents/", include(wagtaildocs_urls)),

    # Wagtail API
    path("api/v2/", api_router.urls),

    # Your custom API routes (OPTIONAL)
    path("api/", include("CONTENT_APP.urls")),  

    # IMPORTANT: Wagtail page serving MUST BE LAST
    path("", include(wagtail_urls)),
]


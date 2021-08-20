"""tmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from accounts.views import CustomAuthToken


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('blog.urls', namespace='blog')),
    path('', include('checkout.urls', namespace='checkout')),
    path('', include('contactus.urls', namespace='contact')),
    path('', include('index.urls', namespace='home')),
    path('', include('product.urls', namespace='product')),
    path('api/', include('product.api.urls')),
    path('api/', include('blog.api.urls')),
    path('api/v1/check-out/', include('checkout.api.urls')),
    path('api/auth/login/', CustomAuthToken.as_view()), 
)



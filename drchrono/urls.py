from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'', include('social_django.urls', namespace='social')),
    url(r'^health_app/', include('health_app.urls')),
    url(r'^admin/', admin.site.urls),
]
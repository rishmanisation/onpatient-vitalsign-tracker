from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^patient', views.patient, name='patient'),
    #url(r'^hr', views.heartrate, name='heartrate'),
    url(r'^bp', views.bloodpressure, name='bloodpressure'),
    url(r'^weight', views.bodyweight, name='weight'),
    url(r'^bmi', views.bodymassindex, name='bodymassindex'),
]
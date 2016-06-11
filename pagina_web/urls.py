#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from tutoriales import views
from django.conf import settings

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.principal, name ='principal'),
    url(r'^tutoriales', views.html, name ='tutoriales'),
    url(r'^descargas', views.descargas, name ='descargas'),


]

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from tutoriales import views
from django.conf import settings

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.principal, name ='principal'),
    url(r'^html', views.html, name ='html'),
    url(r'^css', views.css, name ='css'),


]

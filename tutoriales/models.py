#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Tutoriales(models.Model):
	titulo = models.CharField(max_length=100)
	video = models.FileField(upload_to='documents/%Y/%m/%d')
	capitulo = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.titulo

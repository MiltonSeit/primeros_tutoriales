#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Tutoriales(models.Model):
	titulo = models.CharField(max_length=100)
	direccion = models.URLField(blank=True, null=True)
	capitulo = models.IntegerField(blank=True, null=True)


	def __str__(self):
		return self.titulo

class Descargas(models.Model):
	titulo = models.CharField(max_length=100)
	direccion = models.URLField(blank=True, null=True)
	capitulo = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.titulo

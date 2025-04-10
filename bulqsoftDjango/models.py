from cms.models.pluginmodel import CMSPlugin

from django.db import models

class IconRow(CMSPlugin):
    svg = models.FileField(upload_to='icons/')
    width = models.IntegerField(default=80)
    height = models.IntegerField(default=11)
    is_padded = models.BooleanField(default=True)
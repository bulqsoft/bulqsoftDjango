from cms.models.pluginmodel import CMSPlugin

from django.db import models

class IconRow(CMSPlugin):
    svg = models.FileField(upload_to='icons/')
    width = models.IntegerField(default=80)
    height = models.IntegerField(default=11)
    is_padded = models.BooleanField(default=True)


class AttributeItem(CMSPlugin):
    title = models.CharField(max_length=50, default='')
    body = models.CharField(max_length=255, default='')
    icon_class = models.CharField(max_length=50, default='lqd-icn-ess icon-lqd-mobile')


class AccordionItem(CMSPlugin):
    title = models.CharField(max_length=50, default='')
    body = models.CharField(max_length=255, default='')
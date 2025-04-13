from cms.models.pluginmodel import CMSPlugin
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField

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



class BannerSlider(CMSPlugin):
    def copy_relations(self, oldinstance):
        for slide in oldinstance.slides.all():
            slide.pk = None
            slide.slider = self
            slide.save()
    
    def shown(self):
        return BannerSlide.objects.filter(slider=self, shown=True)


class BannerSlide(models.Model):
    slider = models.ForeignKey(BannerSlider, related_name='slides', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    label = models.CharField(max_length=100)
    image = FilerImageField(on_delete=models.CASCADE, related_name='banner_images', blank=True, null=True)
    shown = models.BooleanField(default=True)

    def __str__(self):
        return self.title
from cms.models.pluginmodel import CMSPlugin
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField

from django.db import models


class IconRow(CMSPlugin):
    def copy_relations(self, oldinstance):
        for icon in oldinstance.icons.all():
            icon.pk = None  # Create a new DB row
            icon.icon_row = self  # Point to the new IconRow instance
            icon.save()

    def shown(self):
        return self.icons.filter(shown=True)
    
class Icon(models.Model):
    svg = models.FileField(upload_to='icons/')
    width = models.IntegerField(default=80)
    height = models.IntegerField(default=11)
    is_padded = models.BooleanField(default=True)
    shown = models.BooleanField(default=True)
    icon_row = models.ForeignKey(IconRow, related_name='icons', on_delete=models.CASCADE)




class AttributeItem(CMSPlugin):
    title = models.CharField(max_length=50, default='')
    body = models.CharField(max_length=255, default='')
    icon_class = models.CharField(max_length=50, default='lqd-icn-ess icon-lqd-mobile')


class AccordionItem(CMSPlugin):
    title = models.CharField(max_length=50, default='')
    body = models.CharField(max_length=255, default='')



class BannerSlider(CMSPlugin):
    def copy_relations(self, oldinstance):
        for slide in oldinstance.slides.all():  # uses related_name='slides'
            slide.pk = None
            slide.slider = self
            slide.save()

    def shown(self):
        return self.slides.filter(shown=True)


class BannerSlide(models.Model):
    slider = models.ForeignKey(BannerSlider, related_name='slides', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    label = models.CharField(max_length=100)
    image = FilerImageField(on_delete=models.CASCADE, related_name='banner_images', blank=True, null=True)
    shown = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    





class Integration(CMSPlugin):
    title = models.CharField(max_length=255, default="Integration")
    subtitle = models.CharField(max_length=255, default="We collaborate with Top E-Commerce CMS in the World")

    def copy_relations(self, oldinstance):
        for integration in oldinstance.integration.all():  # using related_name
            integration.pk = None  # duplicate
            integration.Integration = self  # assign new parent
            integration.save()

    def shown(self):
        return self.integration.filter(shown=True) 
    
class Integrations(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = FilerImageField(on_delete=models.CASCADE, related_name='integration_images', blank=True, null=True)
    image_height = models.IntegerField(default=1000)
    image_width = models.IntegerField(default=720)
    Integration = models.ForeignKey(Integration, related_name='integration', on_delete=models.CASCADE, null=True)
    shown = models.BooleanField(default=True)
    link = models.CharField(max_length=2550, default='#')


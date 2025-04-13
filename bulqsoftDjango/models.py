from cms.models.pluginmodel import CMSPlugin
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField

from django.db import models


class IconRow(CMSPlugin):
    def copy_relations(self, oldinstance):
        for icon in oldinstance.icons.all():
            icon.pk = None
            icon.icon_row = self
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
        for slide in oldinstance.slides.all():
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
        for integration in oldinstance.integration.all():
            integration.pk = None
            integration.Integration = self
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


class StepContainer(CMSPlugin):
    def copy_relations(self, oldinstance):
        for step in oldinstance.steps.all():
            step.pk = None
            step.container = self
            step.save()

    def shown(self):
        return self.steps.filter(shown=True) 
    

class Step(models.Model):
    title = models.CharField(max_length=255)
    title_line_2 = models.CharField(max_length=255, blank=True, null=True)
    body = models.CharField(max_length=2550)
    container = models.ForeignKey(StepContainer, related_name='steps', on_delete=models.CASCADE, null=True)
    shown = models.BooleanField(default=True)
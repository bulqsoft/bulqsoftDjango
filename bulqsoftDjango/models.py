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




class Attribute(CMSPlugin):
    title = models.CharField(max_length=50, default='Pioneering Tomorrow\'s Software Today')
    body = models.CharField(max_length=255, default='The Most Important Attributes That Differentiates Us From Others.')

    def copy_relations(self, oldinstance):
        for item in oldinstance.attributeitems.all():
            item.pk = None
            item.attribute = self
            item.save()

    def shown(self):
        return self.attributeitems.filter(shown=True)

class AttributeItem(models.Model):
    title = models.CharField(max_length=50, default='')
    body = models.CharField(max_length=255, default='')
    icon_class = models.CharField(max_length=50, default='lqd-icn-ess icon-lqd-mobile')
    attribute = models.ForeignKey(Attribute, related_name='attributeitems', on_delete=models.CASCADE)



class Accordion(CMSPlugin):
    image = FilerImageField(on_delete=models.CASCADE, related_name='accordion_images', blank=True, null=True)
    image_height = models.IntegerField(default=979)
    image_width = models.IntegerField(default=1283)
    image_label = models.CharField(max_length=20, default='Lets\'s chat')
    label = models.CharField(max_length=20, default='ONE PLATFORM UNITES ALL')
    title = models.CharField(max_length=255, default='Join Game Changing Store Management')
    highlighted_title = models.CharField(max_length=255, default='Ecosystem')
    title_post_highlight = models.CharField(max_length=255, default='by Bulqsoft')
    def copy_relations(self, oldinstance):
        for item in oldinstance.accordionitems.all():
            item.pk = None
            item.accordion = self
            item.save()

    def shown(self):
        return self.accordionitems.filter(shown=True)

class AccordionItem(models.Model):
    title = models.CharField(max_length=50, default='')
    body = models.CharField(max_length=255, default='')
    shown = models.BooleanField(default=True)
    accordion = models.ForeignKey(Accordion, related_name='accordionitems', on_delete=models.CASCADE)



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




class BananaBanner(CMSPlugin):
    back_text = models.CharField(max_length=255)
    front_text = models.CharField(max_length=255)
    front_text2 = models.CharField(max_length=255)
    image = FilerImageField(on_delete=models.CASCADE, related_name='banana_images', blank=True, null=True)
    image_height = models.IntegerField(default=1123)
    image_width = models.IntegerField(default=2080)
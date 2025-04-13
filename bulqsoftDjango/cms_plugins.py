from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import *
from django.utils.functional import cached_property
from django.contrib import admin




class IconInline(admin.StackedInline):
    model = Icon
    extra = 1
    max_num = 6
@plugin_pool.register_plugin
class IconRowPlugin(CMSPluginBase):
    model = IconRow
    name = _("Icon Row")
    render_template = "plugins/IconRow.html"
    inlines = [IconInline]
    allow_children = False




@plugin_pool.register_plugin
class AttributeItemPlugin(CMSPluginBase):
    model = AttributeItem
    render_template = "plugins/AttributeItem.html"
    cache = False



@plugin_pool.register_plugin
class AccordionItemPlugin(CMSPluginBase):
    model = AccordionItem
    render_template = "plugins/AccordionItem.html"
    cache = False

    def render(self, context, instance, placeholder):
        first_id = AccordionItem.objects.order_by('id').values_list('id', flat=True).first()
        context['is_first'] = instance.id == first_id
        context['instance'] = instance
        return context
    


class BannerSlideInline(admin.StackedInline):
    model = BannerSlide
    extra = 1


@plugin_pool.register_plugin
class BannerSliderPlugin(CMSPluginBase):
    model = BannerSlider
    name = _("Banner Slider")
    render_template = "plugins/BannerSlider.html"
    inlines = [BannerSlideInline]
    allow_children = False




class IntegrationsInline(admin.StackedInline):
    model = Integrations
    extra = 1


@plugin_pool.register_plugin
class IntegrationPlugin(CMSPluginBase):
    model = Integration
    name = _("Integration Plugin")
    render_template = "plugins/Integration.html"
    inlines = [IntegrationsInline]
    allow_children = False
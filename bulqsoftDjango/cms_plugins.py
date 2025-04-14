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




class AttributeInline(admin.StackedInline):
    model = AttributeItem
    extra = 1
@plugin_pool.register_plugin
class AttributePlugin(CMSPluginBase):
    model = Attribute
    name = _("Attribute")
    render_template = "plugins/Attribute.html"
    inlines = [AttributeInline]
    allow_children = False



class AccordionInline(admin.StackedInline):
    model = AccordionItem
    extra = 1
@plugin_pool.register_plugin
class AccordionPlugin(CMSPluginBase):
    model = Accordion
    name = _("Accordion")
    render_template = "plugins/Accordion.html"
    inlines = [AccordionInline]
    allow_children = False


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




class StepInline(admin.StackedInline):
    model = Step
    extra = 1
    max_num = 3


@plugin_pool.register_plugin
class StepContainer(CMSPluginBase):
    model = StepContainer
    name = _("Step Plugin")
    render_template = "plugins/StepContainer.html"
    inlines = [StepInline]
    allow_children = False




@plugin_pool.register_plugin
class BananaBanner(CMSPluginBase):
    model = BananaBanner
    name = _("Banana Banner")
    render_template = "plugins/BananaBanner.html"
    allow_children = False
    cache= False
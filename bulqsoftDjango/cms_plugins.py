from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import *
from django.utils.functional import cached_property

@plugin_pool.register_plugin
class IconRowPlugin(CMSPluginBase):
    model = IconRow
    render_template = "plugins/IconRow.html"
    cache = False

    def save_model(self, request, obj, form, change):
        placeholder = obj.placeholder
        if placeholder:
            count = placeholder.get_plugins().filter(plugin_type=self.__class__.__name__).count()
            if obj.pk:  # if editing, exclude this instance
                count -= 1
            if count >= 6:
                raise ValidationError(f"You can only add 6 plugins to {self.name}")
        super().save_model(request, obj, form, change)



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
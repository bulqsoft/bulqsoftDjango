from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import IconRow

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

from django.conf import settings

from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu

main_menu = PluginMenuItem(
        link='plugins:netbox_plugin_importer:catalog',
        link_text='Custom Object Catalog',
    )

groups = [(("Catalog"), (main_menu,))]


menu = PluginMenu(
    label="Custom Objects Library",
    groups=tuple(groups),
    icon_class="mdi mdi-toy-brick-outline",
)


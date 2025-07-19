from netbox.plugins import PluginConfig
from .version import __version__


class NetBoxPluginImporterConfig(PluginConfig):

    name = 'netbox_plugin_importer'
    verbose_name = 'NetBox Plugin Importer'
    description = ''
    version = __version__
    base_url = 'importer'
    min_version = '4.3.0'
    max_version = '4.3.99'

    def ready(self):
        super().ready()

        from .jobs import CatalogPullJob

config = NetBoxPluginImporterConfig

import django_tables2 as tables
from netbox.tables import BaseTable, columns
from .models import COCatalogEntry


class CatalogObjectListTable(BaseTable):
    id = tables.Column(
    )
    name = tables.Column(
    )
    version = tables.Column(
    )

    class Meta(BaseTable.Meta):
        empty_text = ('No custom objects found')
        fields = (
            'id', 'name', 'version'
        )
        default_columns = (
            'id', 'name', 'version'
        )
        # List installed plugins first, then certified plugins, then
        # everything else (with each tranche ordered alphabeticall
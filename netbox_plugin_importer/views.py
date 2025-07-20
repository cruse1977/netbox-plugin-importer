from django.views.generic import View
from .tables import CatalogObjectListTable
from .models import COCatalogEntry
from django.conf import settings
from utilities.htmx import htmx_partial
from django.shortcuts import render
import json
import logging

class CatalogObjectListView(View):

    def get(self, request):
        logger = logging.getLogger("netbox")
        q = request.GET.get('q', None)

        with open(f"{settings.MEDIA_ROOT}/custom-objects-catalog.json", "r") as f:
            customobjects = json.load(f)

        newobjects = []
        for customobject in customobjects['data']:
            newobjects.append(COCatalogEntry(
                id=customobject['id'],
                name=customobject['name'],
                version=customobject['version']
            ))
        logger.debug(f"New objects: {newobjects}")

        table = CatalogObjectListTable(newobjects, user=request.user)
        table.configure(request)

        # If this is an HTMX request, return only the rendered table HTML
        if htmx_partial(request):
            return render(request, 'htmx/table.html', {
                'table': table,
            })

        return render(request, 'netbox_plugin_importer/catalog_list.html', {
            'table': table,
        })

class CatalogObjectInstallView(View):

    def get(self, request):
        return render(request, 'netbox_plugin_importer/catalog_install.html')



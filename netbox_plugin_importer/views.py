from django.views.generic import View
from .tables import CatalogListTable

class CatalogListView(View):

    def get(self, request):
        q = request.GET.get('q', None)

        table = CatalogListTable(plugins, user=request.user)
        table.configure(request)

        # If this is an HTMX request, return only the rendered table HTML
        if htmx_partial(request):
            return render(request, 'htmx/table.html', {
                'table': table,
            })

        return render(request, 'catalog_list.html', {
            'table': table,
        })




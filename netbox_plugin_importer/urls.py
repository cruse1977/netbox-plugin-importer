from django.urls import include, path


from . import views

app_name = 'netbox_plugin_importer'
urlpatterns = (
    path('catalog/', views.CatalogObjectListView.as_view(), name='catalog'),
    path('catalog/install/', views.CatalogObjectInstallView.as_view(), name='catalog_install'),
)
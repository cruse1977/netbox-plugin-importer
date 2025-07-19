from django.urls import include, path


from . import views

app_name = 'netbox_plugin_importer'
urlpatterns = (
    path('catalog/', views.CatalogListView.as_view(), name='catalog'),
)
from django.conf.urls import include
from django.conf.urls.defaults import patterns, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # dinamic pages
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^add/$', 'budgetelem.views.add', name='add'),
    url(r'^budget/bubble/(?P<document_id>\d+)', 'budgetelem.views.view_one'),
    url(r'^budget/table/(?P<document_id>\d+)', 'budgetelem.views.table'),
    url(r'^budget/tree/(?P<document_id>\d+)', 'budgetelem.views.view_two'),
    url(r'^budget/csv/(?P<document_id>\d+)', 'budgetelem.views.generate_csv'),
    url(r'^budget/json/(?P<document_id>\d+)', 'budgetelem.views.generate_json'),
    url(r'^region/(?P<region_code>\d+)', 'budgetelem.views.region'),
    url(r'^budget/(?P<budget_id>\d+)', 'budgetelem.views.budget'),
    url(r'^localname/(?P<local_name>\D+)', 'budgetelem.views.local_name'),
    url(r'^all/', 'budgetelem.views.all_budgets'),
    url(r'^federal/', 'budgetelem.views.federal'),
    url(r'^regional/', 'budgetelem.views.regional'),
    url(r'^regional-map/', 'budgetelem.views.regional_map'),
    url(r'^local/', 'budgetelem.views.local'),
    url(r'^local-map/', 'budgetelem.views.local_map'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
    url(r'^admin/', include(admin.site.urls)),
    #Static pages
    url(r'^help/', 'budgetelem.static_views.help'),
    url(r'^helpdoc/', 'budgetelem.static_views.helpdoc'),
    url(r'^about/', 'budgetelem.static_views.about'),
    url(r'^contacts/', 'budgetelem.static_views.contacts'),
    url(r'^intentions/', 'budgetelem.static_views.intentions'),    
    url(r'^donate/', 'budgetelem.static_views.donate'),
    url(r'^', 'budgetelem.views.index', name='index'),
)

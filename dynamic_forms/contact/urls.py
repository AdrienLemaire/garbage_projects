# from django
from django.conf.urls.defaults import *

urlpatterns = patterns('contact.views',
    url(r'^$', 'list_contacts', name="list_contacts"),
    url(r'^(?P<pk>[\d]+)$', 'show_contact', name="show_contact"),
    url(r'^add/$', 'add_contact', name="add_contact"),
    url(r'^add/(?P<type_form>[\w]+)/$', 'add_contact', name="add_contact"),
)

from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       # url(r'^mysite/', include('mysite.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       #making a homepage
                       url(r'^pages/', include('pages.urls')),

                       #my way of making index.html. Probably wrong. xD
                       url(r'.*?', include('pages.urls')),
                       )

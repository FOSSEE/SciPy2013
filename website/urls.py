from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Home page
    url(r'^$', 'website.views.home_page', name='home'),
    
    # About Section
    url(r'^venue/$', 'website.views.venue_page', name='venue'),
    url(r'^reaching-venue/$', 'website.views.reaching_venue_page', name='reaching-venue'),
    url(r'^contact/$', 'website.views.contact_page', name='contact'),
    
    # Call for papers
    url(r'^call-for-proposals/$', 'website.views.call_for_papers_page', name='call-for-proposals'),
    
    # Conference Section
    url(r'^schedule/$', 'website.views.schedule_page', name='schedule'),
    url(r'^invited-speakers/$', 'website.views.invited_speakers_page', name='invited-speakers'),
    url(r'^abstracts/$', 'website.views.list_of_abstracts', name='list-abstracts'),
    url(r'^abstract-details/(?P<paper_id>\d+)/$', 'website.views.abstract_details', name="abstract-details"),
    url(r'^accepted-abstracts/$', 'website.views.accepted_abstracts_page', name='accepted-abstracts'),
    
    # Register
    url(r'^register/$', 'website.views.register_page', name='register'),
    
    # Sponsors
    url(r'^sponsors/$', 'website.views.sponsors_page', name='sponsors'),

    # ajax
    url(r'^ajax-get-abstract/$', 'website.views.ajax_get_abstract', name='ajax_get_abstract'),
)

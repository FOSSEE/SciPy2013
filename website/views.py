from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

# Home section
def home_page(request):
    return render_to_response('index.html')

# About section
def venue_page(request):
    return render_to_response('venue.html')

def reaching_venue_page(request):
    return render_to_response('reaching_venue.html')

def contact_page(request):
    return render_to_response('contact.html')

# Call for papers
def call_for_papers_page(request):
    status = ''
    if 'status' in request.GET:
        status = request.GET['status']

    if request.user.is_anonymous():
        current_user = "anonymous"
    else:
        current_user = request.user

    context = {
      'status': status,
      'current_user': current_user
    }
    return render_to_response('papers.html', context)

# Conference Section
def schedule_page(request):
    return render_to_response('schedule.html')

def invited_speakers_page(request):
    return render_to_response('invited_speakers.html')

def accepted_abstracts_page(request):
    return render_to_response('accepted_abstracts.html')

# Register
def register_page(request):
    return render_to_response('register_2013.html')

# Sponsors
def sponsors_page(request):
    return render_to_response('sponsors.html')

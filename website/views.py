from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from models import *

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
    context = {}
    papers = Paper.objects.filter(verified=True)
    context['papers'] = papers    
    return render_to_response('schedule.html', context)

def invited_speakers_page(request):
    return render_to_response('invited_speakers.html')

def list_of_abstracts(request):
    user = request.user
    context = {}
    reviewers = ['jaidevd', 'prabhu', 'jarrod', 'hardythe1']
    papers = Paper.objects.all()
    if user.username not in reviewers:
        context['papers'] = papers
        return render_to_response('list_abstracts_anonymous.html', context)
    else:
        context['papers'] = papers
        context['user'] = user
        return render_to_response('list_abstracts.html', context)
    
def abstract_details(request, paper_id=None):
    user = request.user
    context = {}
    reviewers = ['jaidevd', 'prabhu', 'jarrod', 'hardythe1']
    if user.username in reviewers:
        context['reviewer'] = True
        paper = Paper.objects.get(id=paper_id)
        comments = Comment.objects.filter(paper=paper)
        if(len(str(paper.attachments))<=0):
            attachment = False
        else:
            attachment = True
        context['paper'] = paper
        context['comments'] = comments
        context['attachment'] = attachment
        context['current_user'] = user
        context.update(csrf(request))
        if request.method == 'POST':
            user_comment = request.POST['comment']
            new_comment = Comment()
            new_comment.paper = paper
            new_comment.comment_by = user
            new_comment.comment = user_comment.replace('\n', '<br>')
            new_comment.save()
            return HttpResponseRedirect('/2013/abstract-details/'+paper_id, context)
        else:
            return render_to_response('abstract_details.html', context)
    else:
        return render_to_response('not_allowed.html', context)
        


def accepted_abstracts_page(request):
    context = {}
    accepted_papers = Paper.objects.filter(verified=True)
    context['papers'] = accepted_papers
    context.update(csrf(request))
    return render_to_response('accepted_abstracts.html', context)

# Register
def register_page(request):
    return render_to_response('register_2013.html')

# Sponsors
def sponsors_page(request):
    return render_to_response('sponsors.html')

@csrf_exempt
def ajax_get_abstract(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        paper = Paper.objects.get(pk=pid)
        context = {
            'paper': paper
        }
    return render_to_response('get-abstract.html', context)


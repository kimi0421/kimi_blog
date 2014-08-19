import os
from django.template import RequestContext
from django.shortcuts import render_to_response

def blog(request):
    ipython_note_book_files = os.listdir('static/ipython_blog/')
    context = RequestContext(request)
    topics_text = list(set([topic.split('.')[0] for topic in ipython_note_book_files]))
    topics_text.sort()
    topics = {'message': open('static/ipython_blog/Decision Tree.html', 'r').read(), 'item_list': topics_text}
    return render_to_response('base.html', topics, context)
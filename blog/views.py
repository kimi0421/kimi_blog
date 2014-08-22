import os
import pandas as pd
from django.template import RequestContext
from django.shortcuts import render_to_response


def sort_date(date_list):
    date_dict = {pd.Timestamp(i): i for i in date_list}
    converted_date_list = date_dict.keys()
    converted_date_list.sort()
    return [date_dict[j] for j in converted_date_list[::-1]]


def blog(request, **kwargs):
    ipython_note_book_files = os.listdir('static/ipython_blog/')
    context = RequestContext(request)
    item_list = {}
    for file_name in ipython_note_book_files:

        if 'ipynb' not in file_name:
            continue
        if 'checkpoints' in file_name:
            continue
        if 'files' in file_name:
            continue

        date = file_name.split('.')[0].split('_')[1].replace('-', ' ')
        name = file_name.split('.')[0].split('_')[0]
        if date not in item_list:
            item_list[date] = [name]
        else:
            item_list[date].append(name)
        item_list[date].sort()

    date_list = item_list.keys()
    sorted_date_list = sort_date(date_list)
    item_list['dates'] = sorted_date_list

    if len(kwargs) == 0:
        subject = item_list[item_list['dates'][0]][0]
    else:
        subject = kwargs['file_name']

    file_name = [i for i in ipython_note_book_files if subject in i and 'html' in i][0]
    message = open('static/ipython_blog/%s' % file_name, 'r').read()
    topic_name = subject
    topics = {'message': message, 'item_list': item_list, 'topic_name': topic_name}
    return render_to_response('base.html', topics, context)
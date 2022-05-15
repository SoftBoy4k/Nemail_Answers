from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    return render(request, 'nemail_answer/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'nemail_answer/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'nemail_answer/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('../')
        
    context = {'form': form}
    return render(request, 'nemail_answer/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data =request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return redirect('nemail_answer:topic', topic_id = topic_id)
    context = {'topic': topic, 'form':form}
    return render(request, 'nemail_answer/new_entry.html', context)        
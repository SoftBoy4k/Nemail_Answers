from django.urls import path
from . import views

app_name = 'nemail_answer'
urlpatterns = [
    # path('index/', views.index, name='index'),
    path('', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
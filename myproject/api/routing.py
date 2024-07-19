from django.urls import re_path
from channels.routing import route
from .consumers import QuestionConsumer,ChoiceConsumer

websocket_urlpatterns = [re_path(r'ws/question_updates/$',QuestionConsumer.as_asgi()),
                         route('websocket.connect',ChoiceConsumer)]
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Question
from .serializers import QuestionSerializer

class QuestionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
         await self.accept()
    async def disconnect(self, close_code):
         pass
    async def send_question_update(self, event):
         message = event["message"]
         await self.send(text_data=json.dumps(message))    
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django import forms
from .models import Question, Choice, Expense
from .forms import  ChoiceForm, QuestionForm
from rest_framework import generics
from .serializers import QuestionSerializer, ChoiceSerializer, ExpenseSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

class ExpenseListCreate(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

@api_view(["GET", "POST", "PUT", "DELETE"])
def get_questions(request):
    if request.method == 'POST':
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'question_update',
            {
                'type': 'send_question_update',
                'message': 'New Question added',
            }
        )
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        question = get_object_or_404(Question, pk=request.data['id'])
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        question = get_object_or_404(Question, pk=request.data['id'])
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class QuestionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_question_update(self, event):
        message = event['message']
        await self.send(text_data=message)

def index(request):
    return render(request, 'hello/index.html')

def task(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def rishi(request):
    return render(request, "Home/index.html")

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect("/tasks")
        else:
            return render(request, "tasks/add.html", {"form": form})
    return render(request, "tasks/add.html", {"form": NewTaskForm()})

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Newtask")

def Questions(request):
    return render(request, "Question/quetion.html", {"questions": Question.objects.all()})

def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/question")
        else:
            return render(request, "Question/addQuestion.html", {"form": form})
    else:
        form = QuestionForm()
        return render(request, 'Question/addQuestion.html', {"form": form})

class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceListCreateView(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

@api_view(["GET", "POST"])
def get_choices(request):
    if request.method == 'POST':
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'choice_update',
            {
                'type': 'send_choice_update',
                'message': 'New choice added',
            }
        )
    choices = Choice.objects.all()
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)

class ChoiceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_choice_update(self, event):
        message = event['message']
        await self.send(text_data=message)

def add_choice(request):
    if request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/choices")
        else:
            return render(request, "Question/addChoice.html", {"form": form})
    else:
        form = ChoiceForm()
        return render(request, 'Question/addChoice.html', {"form": form})

def delete_question(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    except Http404:
        question = None

    if request.method == "POST" and question:
        question.delete()
        return redirect("/question")
    else:
        return render(request, "Question/deleteQuestion.html", {"question": question})

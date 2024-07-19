from rest_framework import serializers
from .models import Question,Choice,Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'date']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice 
        fields = '__all__'      

        
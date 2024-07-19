from django.contrib import admin
from .models import Question,Choice,Expense
admin.site.register(Question) 
admin.site.register(Choice)
admin.site.register(Expense)
# Register your models here.

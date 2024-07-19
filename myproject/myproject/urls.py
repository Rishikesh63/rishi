"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views 
from users import urls
from api.views import QuestionListCreateView,ChoiceListCreateView,delete_question,ExpenseListCreate
from users.views import ProductListCreateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.rishi),
    path("index/",views.index),
    path("tasks/",views.task),
    path("add/",views.add,name="add"),
    path("question/",views.Questions),
    path("add_question/",views.add_question,name="add_question"),
    path('questions/',QuestionListCreateView.as_view(),name='question-list-create'),
    path('choice/',ChoiceListCreateView.as_view(),name='choice-list-create'),
    path('choices/',views.add_choice,name="add_choice"),
    path('question/<int:question_id>/delete/', views.delete_question, name='delete_question'),
    path('user/',include('users.urls')),
    path('create-expense/', ExpenseListCreate.as_view(), name='create-expense'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
]


"""EPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('insertUser', views.insertUser, name='insertUser'),
    path('getUser', views.getUser, name='getUser'),
    path('deleteUser', views.deleteUser, name='deleteUser'),
    path('updateUserPassword', views.updateUserPassword, name='updateUserPassword'),
    path('updateUserApproval', views.updateUserApproval, name='updateUserApproval'),
    path('loginUser', views.loginUser, name='loginUser'),

    path('insertDocusers', views.insertDocusers, name='insertDocusers'),
    path('getDocusers', views.getDocusers, name='getDocusers'),
    path('deleteDocuser', views.deleteDocuser, name='deleteDocuser'),
    path('updateDocuserPassword', views.updateDocuserPassword, name='updateDocuserPassword'),
    path('loginDoctoruser', views.loginDoctoruser, name='loginDoctoruser'),

    path('insertBiodata', views.insertBiodata, name='insertBiodatainsertBiodata'),
    path('getBiodata', views.getBiodata, name='getBiodata'),
    path('updateBiodata', views.updateBiodata, name='updateBiodata'),

    path('insertDoctordata', views.insertDoctordata, name='insertDoctordata'),
    path('getDoctordata', views.getDoctordata, name='getDoctordata'),
    path('updateDoctordata', views.updateDoctordata, name='updateDoctordata'),

    path('insertQuestion', views.insertQuestion, name='insertQuestion'),
    path('getAllQuestions', views.getAllQuestions, name='getAllQuestions'),
    path('getQuestion', views.getQuestion, name='getQuestion'),
    path('updateQuestion', views.updateQuestion, name='updateQuestion'),
    path('deleteQuestion', views.deleteQuestion, name='deleteQuestion'),

    path('insertQuestionOption', views.insertQuestionOption, name='insertQuestionOption'),
    path('getQuestionOption', views.getQuestionOption, name='getQuestionOption'),
    path('updateQuestionOption', views.updateQuestionOption, name='updateQuestionOption'),
    path('deleteQuestionOption', views.deleteQuestionOption, name='deleteQuestionOption'),

    
]

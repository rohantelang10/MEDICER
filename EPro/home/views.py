import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, response
from .models import Users, Doctorusers
def index(request):
    
    return render(request, 'documentation.html')

# CURD Operations of User Table

def insertUser(request):
    if request.method == 'POST':
        email = request.POST.get('UserInstertEmailInput')
        password = request.POST.get('UserInstertPasswordInput')
        # isapproved = request.POST.get('isapproved')
        try:
            user = Users(email = email, password = password, isapproved = 0)
            user.save()
            response = {'status':1, 'msg':"Successfully Done"}
        except:
            response = {'status':0, 'msg':"internal server error"}

        return JsonResponse(response)

def getUser(request):
    # Need to check if database is empty or not!
    try:
        users = Users.objects.values()
        # print('************',type(users[0]))
        # print('-------', users)
        users = list(users)
        # print(type(users))
        response = {'status':1, 'msg':"fatched successfully","userdata":users}
    except:
        response = {'status':0, 'msg':"internal server error"}

    return JsonResponse(response)

def deleteUser(request):
    try:
        id = 9
        toDeleteUser = Users.objects.filter(userid=id)
        print(toDeleteUser, '+++++++++++++++++')
        if len(toDeleteUser)==0:
            response = {'status':1, 'msg':"user not found"}
        else:
            toDeleteUser.delete()
            response = {'status':1, 'msg':"deleted successfully"}
    except:
        response = {'status':0, 'msg':"internal server error"}
    return JsonResponse(response)

def updateUserPassword(request):
    try:
        id = 9
        newPassword = '123456789'
        toUpdateUser = Users.objects.filter(userid=id)
        print(toUpdateUser, '+++++++++++++++++')
        if len(toUpdateUser)==0:
            response = {'status':1, 'msg':"user not found"}
        else:
            toUpdateUser.update(password=newPassword)
            response = {'status':1, 'msg':"updated successfully"}
    except:
        response = {'status':0, 'msg':"internal server error"}
    return JsonResponse(response)

def updateUserApproval(request):
    # if request.method == 'POST':
        # id = 1
    id = request.POST.get('userId')

    try:
        user = Users.objects.filter(userid=id).update(isapproved=1)

        response = {'status':1, 'msg':"user approved successfully"}
    except:
        response = {'status':0, 'msg':"internal server error"}


    return JsonResponse(response)

# CURD of docUsers Table
def insertDocusers(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Doctorusers(docemail = email, docpassword = password)
            user.save()
            response = {'status':1, 'msg':"Successfully Done"}
        except:
            response = {'status':0, 'msg':"internal server error"}

        return JsonResponse(response)

def getDocusers(request):
    # Need to check if database is empty or not!
    try:
        docusers = Doctorusers.objects.values()
        # print('************',type(users[0]))
        # print('-------', users)
        docusers = list(docusers)
        # print(type(users))
        response = {'status':1, 'msg':"fatched successfully","userdata":docusers}
    except:
        response = {'status':0, 'msg':"internal server error"}

    return JsonResponse(response)    

def deleteDocusers(request):
    try:
        id = 1
        toDeleteDocuser = Doctorusers.objects.filter(docuserid=id)
        print(toDeleteDocuser, '+++++++++++++++++')
        if len(toDeleteDocuser)==0:
            response = {'status':1, 'msg':"user not found"}
        else:
            toDeleteDocuser.delete()
            response = {'status':1, 'msg':"deleted successfully"}
    except:
        response = {'status':0, 'msg':"internal server error"}
    return JsonResponse(response)

def updateDocuserPassword(request):
    try:
        id = 2
        newPassword = '123456789'
        toUpdateDocuser = Doctorusers.objects.filter(docuserid=id)
        # print(toUpdateDocuser, '+++++++++++++++++')
        if len(toUpdateDocuser)==0:
            response = {'status':1, 'msg':"user not found"}
        else:
            toUpdateDocuser.update(docpassword=newPassword)
            response = {'status':1, 'msg':"updated successfully"}
    except:
        response = {'status':0, 'msg':"internal server error"}
    return JsonResponse(response)

# Login System
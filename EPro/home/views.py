from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Users
def index(request):
    # users = Users.objects.values()
    # print('************',type(users[0]))
    # print('-------', users)
    # return JsonResponse(users[0])
    users = Users.objects.all()
    context = {
        'users':users
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        isapproved = request.POST.get('isapproved')
        user = Users(email = email, password = password, isapproved = isapproved)
        user.save()
    if request.method == 'GET':
        id = request.GET.get('id')
        Users.objects.filter(userid=id).delete()
    return render(request, 'index.html', context)

def insertDailyRecord(request):
    return render(request, 'insertDailyRecord.html')

def getDailyRecord(request):
    return render(request, 'getDailyRecord.html')

# def user_insert(request):
#     return
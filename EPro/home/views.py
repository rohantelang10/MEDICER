import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, response

from .models import Users, Doctorusers, Biodata, Doctordata, Doctorpatientconnection, Questions, Questionoptions
from django.views.decorators.csrf import csrf_exempt
# Constants
API_SUCCESS_USER_ALREADY_EXIST = 3
API_SUCCESS_USER_NOT_APPROVED = 2
API_SUCCESS_DATA_FOUND = 1
API_SUCCESS_DATA_NOT_FOUND = 0
SERVER_ERROR = 500


def index(request):

    return render(request, 'documentation.html')

# --------------------------------------------------------------------------
# CURD Operations of User Table


@csrf_exempt
def insertUser(request):
    if request.method == 'POST':
        email = request.POST.get('UserInsertEmailInput')
        password = request.POST.get('UserInsertPasswordInput')
        try:
            if(len(Users.objects.filter(email=email, password=password)) == 0):
                user = Users(email=email, password=password, isapproved=0)
                user.save()
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "successfully done"}
            else:
                response = {'status': API_SUCCESS_USER_ALREADY_EXIST,
                            'msg': "user already exist"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def getUser(request):
    # Need to check if database is empty or not!
    if request.method == 'POST':
        id = request.POST.get('GetUserIdInput')
        try:
            users = Users.objects.filter(userid=id)
            if len(users) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': 'user not found'}
            else:
                response = {'status': API_SUCCESS_DATA_FOUND, 'msg': "fatched successfully", "userdata": users.values()[
                    0]}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def deleteUser(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('DeleteUserIdInput')
            toDeleteUser = Users.objects.filter(userid=id)
            if len(toDeleteUser) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "user not found"}
            else:
                toDeleteUser.delete()
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "deleted successfully"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}
        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def updateUserPassword(request):
    # check user id and password is correct or not
    if request.method == 'POST':
        try:
            id = request.POST.get('UpdateUserIdInput')
            newPassword = request.POST.get('UpadateUserPasswordInput')
            toUpdateUser = Users.objects.filter(userid=id)
            if len(toUpdateUser) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "user not found"}
            else:
                toUpdateUser.update(password=newPassword)
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "new password updated successfully"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}
        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def updateUserApproval(request):
    if request.method == 'POST':
        id = request.POST.get('UserApprovalIdInput')
        try:
            user = Users.objects.filter(userid=id)
            if len(user) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "user not found"}
            else:
                user.update(isapproved=1)
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "user approved successfully"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('UserLoginEmailInput')
        password = request.POST.get('UserLoginPasswordInput')
        try:
            user = Users.objects.filter(email=email, password=password)
            if len(user) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "user not found"}
            else:
                user = user.values()[0]
                if user['isapproved'] == 0:
                    response = {
                        'status': API_SUCCESS_USER_NOT_APPROVED, 'msg': "user not approved"}
                else:
                    response = {'status': API_SUCCESS_DATA_FOUND,
                                'msg': "successfully done", 'userId': user['userid']}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')

# --------------------------------------------------------------------------
# CURD of Biodata Table


@csrf_exempt
def insertBiodata(request):
    if request.method == 'POST':
        id = request.POST.get('BiodataInsertIdInput')
        firstname = request.POST.get('BiodataInsertFirstNameInput')
        lastname = request.POST.get('BiodataInsertLastNameInput')
        age = request.POST.get('BiodataInstertAgeInput')
        weight = request.POST.get('BiodataInstertWeightInput')
        isdiabetic = request.POST.get('BiodataInsertIsDiabeticInput')
        try:
            user = Users.objects.filter(userid=id)
            if len(user) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "user not found"}
            else:
                biodata = Biodata(userid=Users(userid=id), firstname=firstname,
                                  lastname=lastname, age=age, weight=weight, isdiabetic=isdiabetic)
                biodata.save()
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "successfully done"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def getBiodata(request):
    # Need to check if database is empty or not!
    if request.method == 'POST':
        userId = request.POST.get('GetUserIdInput')
        try:
            user = Biodata.objects.filter(userid=Users(userid=userId))
            if len(user) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': 'user not found'}
            else:
                response = {'status': API_SUCCESS_DATA_FOUND, 'msg': "fatched successfully", "userdata": user.values()[
                    0]}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def updateBiodata(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('UpdateUserBiodataIdInput')
            firstname = request.POST.get('UpdateUserBiodataFirstnameInput')
            lastname = request.POST.get('UpdateUserBiodataLastnameInput')
            age = request.POST.get('UpdateUserBiodataAgeInput')
            weight = request.POST.get('UpdateUserBiodataWeightInput')
            isdiabetic = request.POST.get('UpdateUserBiodataIsDiabeticInput')
            toUpdateBiodata = Biodata.objects.filter(userid=Users(userid=id))
            if len(toUpdateBiodata) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "user not found"}
            else:
                toUpdateBiodata.update(
                    firstname=firstname, lastname=lastname, age=age, weight=weight, isdiabetic=isdiabetic)
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "biodata updated successfully"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}
        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


# --------------------------------------------------------------------------
# CURD of docUsers Table

@csrf_exempt
def insertDocusers(request):
    if request.method == 'POST':
        email = request.POST.get('DocuserInsertEmailInput')
        password = request.POST.get('DocuserInstertPasswordInput')
        try:
            if len(Doctorusers.objects.filter(docemail=email, docpassword=password)) == 0:
                user = Doctorusers(docemail=email, docpassword=password)
                user.save()
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "successfully done"}
            else:
                response = {'status': API_SUCCESS_USER_ALREADY_EXIST,
                            'msg': "doctor already exist"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def getDocusers(request):
    # Need to check if database is empty or not!
    if request.method == 'POST':
        id = request.POST.get('GetDocuserIdInput')
        try:
            doctor = Doctorusers.objects.filter(docuserid=id)
            if len(doctor) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': 'user not found'}
            else:
                response = {'status': API_SUCCESS_DATA_FOUND, 'msg': "fatched successfully", "userdata": doctor.values()[
                    0]}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def deleteDocuser(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('DeleteDocuserIdInput')
            toDeleteDocuser = Doctorusers.objects.filter(docuserid=id)
            if len(toDeleteDocuser) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "user not found"}
            else:
                toDeleteDocuser.delete()
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "deleted successfully"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}
        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def updateDocuserPassword(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('UpdateDocuserIdInput')
            newPassword = request.POST.get('UpadateDocuserPasswordInput')
            toUpdateDocuser = Doctorusers.objects.filter(docuserid=id)
            if len(toUpdateDocuser) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "user not found"}
            else:
                toUpdateDocuser.update(docpassword=newPassword)
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "new password updated successfully"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}
        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def loginDoctoruser(request):
    if request.method == 'POST':
        email = request.POST.get('DoctorUserLoginEmailInput')
        password = request.POST.get('DoctorUserLoginPasswordInput')
        try:
            user = Doctorusers.objects.filter(
                docemail=email, docpassword=password)
            if len(user) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "doctor user not found"}
            else:
                user = user.values()[0]
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "Successfully Done", 'userId': user['docuserid']}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')

# --------------------------------------------------------------------------
# CURD of doctorData table


@csrf_exempt
def insertDoctordata(request):
    if request.method == 'POST':
        id = request.POST.get('DoctordataInsertIdInput')
        firstname = request.POST.get('DoctordataInsertFirstNameInput')
        lastname = request.POST.get('DoctordataInsertLastNameInput')
        contactnumber = request.POST.get('DoctordataInstertContactNumberInput')
        cliniclocation = request.POST.get(
            'DoctordataInstertClinicLocationInput')
        specialization = request.POST.get(
            'DoctordataInstertSpecializationInput')
        experience = request.POST.get('DoctordataInstertExperienceInput')
        try:
            docuser = Doctorusers.objects.filter(docuserid=id)
            if len(docuser) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "doctor not found"}
            else:
                doc_patient_count = Doctorpatientconnection.objects.filter(
                    docuserid=id).count()
                doctordata = Doctordata(docuserid=Doctorusers(docuserid=id), docfirstname=firstname, doclastname=lastname, contact=contactnumber,
                                        cliniclocation=cliniclocation, specialization=specialization, experience=experience, totalpatient=doc_patient_count)
                doctordata.save()
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "successfully done"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def getDoctordata(request):
    # Need to check if database is empty or not!
    if request.method == 'POST':
        docUserId = request.POST.get('GetDocdataIdInput')
        try:
            docuser = Doctordata.objects.filter(
                docuserid=Doctorusers(docuserid=docUserId))
            if len(docuser) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': 'doctor not found'}
            else:
                response = {'status': API_SUCCESS_DATA_FOUND, 'msg': "fatched successfully", "doctordata": docuser.values()[
                    0]}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def updateDoctordata(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('DoctordataUpdataIdInput')
            firstname = request.POST.get('DoctordataUpdateFirstNameInput')
            lastname = request.POST.get('DoctordataUpdateLastNameInput')
            contactnumber = request.POST.get(
                'DoctordataUpdateContactNumberInput')
            cliniclocation = request.POST.get(
                'DoctordataUpdateClinicLocationInput')
            specialization = request.POST.get(
                'DoctordataUpdateSpecializationInput')
            experience = request.POST.get('DoctordataUpdateExperienceInput')
            toUpdateDoctordata = Doctordata.objects.filter(
                docuserid=Doctorusers(docuserid=id))
            if len(toUpdateDoctordata) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "user not found"}
            else:
                toUpdateDoctordata.update(
                    docfirstname=firstname, doclastname=lastname, contact=contactnumber,
                    cliniclocation=cliniclocation, specialization=specialization, experience=experience)
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "doctor data updated successfully"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}
        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


# --------------------------------------------------------------------------
# CURD of Question table
@csrf_exempt
def insertQuestion(request):
    if request.method == 'POST':
        docUserId = request.POST.get('QuestionInsertDocUserIdInput')
        questionText = request.POST.get('QuestionInsertQuestionTextInput')
        try:
            doctor = Doctorusers.objects.filter(docuserid=docUserId)
            if len(doctor) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "doctor not found"}
            else:
                questionInsert = Questions(docuserid=Doctorusers(docuserid=docUserId), questiontext=questionText);
                questionInsert.save()
                response = {'status': API_SUCCESS_DATA_FOUND,
                                'msg': "successfully done"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')
@csrf_exempt
def getQuestion(request):
    if request.method == 'POST':
        questionId = request.POST.get('QuestionGetQuestionIdInput')
        try:
            question = Questions.objects.filter(questionid=questionId)
            questionOptions = Questionoptions.objects.filter(questionid=questionId)
            if len(question) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "question not found"}
            else:
                questionOptions = Questionoptions.objects.filter(questionid=questionId)
                optionsList = [option for option in questionOptions.values()]
                response = {'status': API_SUCCESS_DATA_FOUND, 'msg': "fatched successfully", "questionDetails": question.values()[
                    0], "options":optionsList}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def getAllQuestions(request):
    if request.method == 'POST':
        docUserId = request.POST.get('AllQuestionGetDocIdInput')
        print(docUserId)
        
        # question = Questions.objects.filter(docuserid=docUserId).select_related('Questionoptions').values('questionid', 'questiontext', 'optionid', 'optiontext');
        questions = Questions.objects.filter(docuserid=docUserId).values()
        questionData = {}
        for que in questions:
            print(que)
            options = Questionoptions.object.filter(questionid=Questions(questionid=que))
        # print(question)
        # if len(question) == 0:
        #     response = {'status': API_SUCCESS_DATA_NOT_FOUND,
        #                 'msg': "questions not found"}
        # else:
        #     # questionOptions = Questionoptions.objects.filter(questionid=questionId)
        #     # optionsList = [option for option in questionOptions.values()]
        #     response = {'status': API_SUCCESS_DATA_FOUND, 'msg': "fatched successfully", "questionDetails": question.values()}
        # except:
        #     response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


@csrf_exempt
def updateQuestion(request):
    if request.method == 'POST':
        try:
            questionId = request.POST.get('QuestionUpdateQuestionIdInput')
            questionText = request.POST.get('QuestionUpdateQusetionTextInput')
            toUpdateQuestion = Questions.objects.filter(questionid=questionId)
            # checkDoctor = Doctorusers.objects.filter(docuserid = docUserId)
            if len(toUpdateQuestion) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "question not found"}
            else:
                toUpdateQuestion.update(questiontext=questionText)
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "question updated successfully"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}
        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')

@csrf_exempt
def deleteQuestion(request):
    if request.method == 'POST':
        try:
            questionId = request.POST.get('QuestionDeleteQuestionIdInput')
            toDeleteQuestion = Questions.objects.filter(questionid=questionId)
            if len(toDeleteQuestion) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "question not found"}
            else:
                toDeleteQuestion.delete()
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "deleted successfully"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}
        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')


# CURD of Question Option table
@csrf_exempt
def insertQuestionOption(request):
    if request.method == 'POST':
        questionId = request.POST.get('QuestionOptionInsertQuestionIdInput')
        OptionText = request.POST.get('QuestionOptionInsertOptionTextInput')
        try:
            question = Questions.objects.filter(questionid=questionId)
            if len(question) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "question not found"}
            else:
                questionOptionInsert = Questionoptions(questionid=Questions(questionid=questionId), optiontext=OptionText);
                questionOptionInsert.save()
                question.update(totaloptions=int(question.values()[0]["totaloptions"])+1)
                response = {'status': API_SUCCESS_DATA_FOUND,
                                'msg': "successfully done"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')
@csrf_exempt
def getQuestionOption(request):
    if request.method == 'POST':
        optionId = request.POST.get('QuestionOptionGetQuestionOptionIdInput')
        try:
            questionOption = Questionoptions.objects.filter(optionid=optionId)
            if len(questionOption) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "question option not found"}
            else:
                response = {'status': API_SUCCESS_DATA_FOUND, 'msg': "fatched successfully", "question Option": questionOption.values()[
                    0]}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}

        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')

@csrf_exempt
def updateQuestionOption(request):
    if request.method == 'POST':
        try:
            optionId = request.POST.get('QuestionOptionUpdateOptionIdInput')
            optionText = request.POST.get('QuestionOptionUpdateOptionTextInput')
            toUpdateOption = Questionoptions.objects.filter(optionid=optionId)
            # checkDoctor = Doctorusers.objects.filter(docuserid = docUserId)
            if len(toUpdateOption) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "question option not found"}
            else:
                toUpdateOption.update(optiontext=optionText)
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "question option updated successfully"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}
        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')

@csrf_exempt
def deleteQuestionOption(request):
    if request.method == 'POST':
        try:
            optionId = request.POST.get('QuestionOptionDeleteOptionIdInput')
            toDeleteOption = Questionoptions.objects.filter(optionid=optionId)
            if len(toDeleteOption) == 0:
                response = {'status': API_SUCCESS_DATA_NOT_FOUND,
                            'msg': "question option not found"}
            else:
                toDeleteOption.delete()
                response = {'status': API_SUCCESS_DATA_FOUND,
                            'msg': "deleted successfully"}
        except:
            response = {'status': SERVER_ERROR, 'msg': "internal server error"}
        return JsonResponse(response)
    else:
        return render(request, 'documentation.html')
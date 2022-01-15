from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Users(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    isapproved = models.IntegerField(db_column='isApproved')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'

class Biodata(models.Model):
    userid = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='userId', unique=True, primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    age = models.IntegerField()
    weight = models.FloatField()
    isdiabetic = models.IntegerField(db_column='isDiabetic')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'biodata'

class Doctorusers(models.Model):
    docuserid = models.AutoField(db_column='docUserId', primary_key=True)  # Field name made lowercase.
    docemail = models.CharField(db_column='docEmail', max_length=50)  # Field name made lowercase.
    docpassword = models.CharField(db_column='docPassword', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctorusers'

class Doctordata(models.Model):
    docuserid = models.ForeignKey('Doctorusers', on_delete=models.CASCADE, db_column='docUserId', primary_key=True, unique=True)  # Field name made lowercase.
    docfirstname = models.CharField(db_column='docFirstName', max_length=50)  # Field name made lowercase.
    doclastname = models.CharField(db_column='docLastName', max_length=50)  # Field name made lowercase.
    contact = models.TextField()
    cliniclocation = models.TextField(db_column='clinicLocation')  # Field name made lowercase.
    specialization = models.CharField(max_length=50)
    experience = models.IntegerField()
    totalpatient = models.IntegerField(db_column='totalPatient')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctordata'

class Doctorpatientconnection(models.Model):
    docuserid = models.ForeignKey('Doctorusers', on_delete=models.CASCADE, db_column='docUserId', primary_key=True, unique=True)  # Field name made lowercase.
    patientuserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='patientUserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctorpatientconnection'

class Questionoptions(models.Model):
    optionid = models.AutoField(db_column='optionId', primary_key=True)  # Field name made lowercase.
    questionid = models.ForeignKey('Questions', models.DO_NOTHING, db_column='questionId')  # Field name made lowercase.
    optiontext = models.TextField(db_column='optionText')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questionoptions'


class Questions(models.Model):
    questionid = models.AutoField(db_column='questionId', primary_key=True)  # Field name made lowercase.
    docuserid = models.ForeignKey(Doctorusers, on_delete=models.CASCADE, db_column='docUserId')  # Field name made lowercase.
    # catagoryid = models.IntegerField(db_column='catagoryId')  # Field name made lowercase.
    questiontext = models.TextField(db_column='questionText')  # Field name made lowercase.
    totaloptions = models.IntegerField(db_column='totalOptions')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questions'


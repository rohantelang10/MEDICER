# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Biodata(models.Model):
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    age = models.IntegerField()
    weight = models.FloatField()
    isdiabetic = models.IntegerField(db_column='isDiabetic')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'biodata'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doctordata(models.Model):
    docuserid = models.ForeignKey('Doctorusers', models.DO_NOTHING, db_column='docUserId')  # Field name made lowercase.
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
    docuserid = models.ForeignKey('Doctorusers', models.DO_NOTHING, db_column='docUserId')  # Field name made lowercase.
    patientuserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='patientUserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctorpatientconnection'


class Doctorusers(models.Model):
    docuserid = models.AutoField(db_column='docUserId', primary_key=True)  # Field name made lowercase.
    docemail = models.CharField(db_column='docEmail', max_length=50)  # Field name made lowercase.
    docpassword = models.CharField(db_column='docPassword', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctorusers'


class Questionoptions(models.Model):
    optionid = models.AutoField(db_column='optionId', primary_key=True)  # Field name made lowercase.
    questionid = models.ForeignKey('Questions', models.DO_NOTHING, db_column='questionId')  # Field name made lowercase.
    optiontext = models.TextField(db_column='optionText')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questionoptions'


class Questions(models.Model):
    questionid = models.AutoField(db_column='questionId', primary_key=True)  # Field name made lowercase.
    docuserid = models.ForeignKey(Doctorusers, models.DO_NOTHING, db_column='docUserId')  # Field name made lowercase.
    catagoryid = models.IntegerField(db_column='catagoryId')  # Field name made lowercase.
    questiontext = models.TextField(db_column='questionText')  # Field name made lowercase.
    totaloptions = models.IntegerField(db_column='totalOptions')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questions'


class Users(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    isapproved = models.IntegerField(db_column='isApproved')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'

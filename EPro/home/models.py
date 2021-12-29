from django.db import models

# Create your models here.
class Users(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    isapproved = models.IntegerField(db_column='isApproved')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'

class Doctorusers(models.Model):
    docuserid = models.AutoField(db_column='docUserId', primary_key=True)  # Field name made lowercase.
    docemail = models.CharField(db_column='docEmail', max_length=50)  # Field name made lowercase.
    docpassword = models.CharField(db_column='docPassword', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctorusers'
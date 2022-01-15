from django.contrib import admin
from .models import Biodata, Doctordata, Doctorpatientconnection, Doctorusers, Users
# Register your models here.
admin.site.register(Users)
admin.site.register(Biodata)
admin.site.register(Doctorusers)
admin.site.register(Doctordata)
admin.site.register(Doctorpatientconnection)
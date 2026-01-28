from django.contrib import admin

from vege.models import *

admin.site.register(Students)
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Subject)


class SubjectmakrsAdmin(admin.ModelAdmin):
    list_display= ['students','subject','marks']

admin.site.register(StudentsMark,SubjectmakrsAdmin)
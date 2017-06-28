#coding=utf-8
from django.contrib import admin
from bbx.models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('company', 'filiale', 'category', 'date', 'arrival_flight_number', \
                    'depart_flight_number', 'ac_type', 'ac_number', 'sector_number', \
                    'note_number_1', 'note_number_2', 'note_number_3', \
                    'description')
    filedsets =(
        (None,{
        'fields' :('company', 'filiale', 'category', 'date', 'arrival_flight_number', \
                    'depart_flight_number', 'ac_type', 'ac_number', 'sector_number', \
                    'note_number_1', 'note_number_2', 'note_number_3', \
                    'description', 'man_hour')
        }),
        ('Advance',{
            'classes': ('collapse',),
            'fields':('ground_equipment', 'oil', 'hydraulic', 'deicing_fluid'),
        }),
    )

admin.site.register(bbx_info, AuthorAdmin)

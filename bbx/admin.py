#coding=utf-8
from django.contrib import admin
from bbx.models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('company', 'filiale', 'category', 'date', 'arrival_flight_number', \
                    'depart_flight_number', 'ac_type', 'ac_number', 'sector_number', \
                    'description')

    fieldsets = (
        ('基本信息',{'fields' : ('company', 'filiale', 'category', 'date', 'arrival_flight_number', 'depart_flight_number', 'ac_type', 'ac_number', 'sector_number', 'routine_note_number', 'non_routine_note_number_1', 'non_routine_note_number_2', 'non_routine_note_number_3', 'non_routine_note_number_4', 'non_routine_note_number_5', 'description', 'man_hour',)
               }
         ),
        ('地面设备',{'classes': ('collapse',),
                    'fields': ('hangar_time_range', 'hanger_hour', 'runup_ramp_time_range', 'runup_ramp_big_25_time', 'runup_ramp_small_25_time', 'gpu', 'transfer', 'ground_power_unit', 'tow_tug', 'towbar', 'towing_push_tractor', 'seat_elevating_truck', 'forklift', 'air_conditioning', 'pallet_jack', 'truck', 'ndt', 'air_starter', 'lifting_platform_truck', 'small_tow_cart', 'cherry_picker', 'platform', 'jack', 'borescope', 'generator_and_light_source', 'oil_service_cart', 'high_cherry_picker')}),
        ('耗材',{'classes': ('collapse',),
                    'fields': ('oil', 'hydraulic', 'deicing_fluid',)})
    )


admin.site.register(bbx_info, AuthorAdmin)

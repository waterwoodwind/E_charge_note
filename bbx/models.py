#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class bbx_info(models.Model):
    company = models.CharField(max_length=2, verbose_name=u'公司')
    filiale = models.CharField(max_length=20, verbose_name=u'分公司', blank=True)
    category = models.CharField(max_length=10, verbose_name=u'类别')
    date = models.DateField(u'日期')
    arrival_flight_number = models.CharField(max_length=5, verbose_name=u'进港航班', blank= True, null=True)
    depart_flight_number = models.CharField(max_length=5, verbose_name=u'离港航班', blank= True, null=True)
    ac_type = models.CharField(max_length=10, verbose_name=u'机型')
    ac_number = models.CharField(max_length=4, verbose_name=u'机号')
    sector_number = models.CharField(max_length=10, verbose_name=u'航段编号')
    routine_note_number = models.CharField(max_length=10, verbose_name=u'例行收费单编号',blank=True)
    non_routine_note_number_1 = models.CharField(max_length=10, verbose_name=u'非例行收费单编号1',blank=True)
    non_routine_note_number_2 = models.CharField(max_length=10, verbose_name=u'非例行收费单编号2',blank=True)
    non_routine_note_number_3 = models.CharField(max_length=10, verbose_name=u'非例行收费单编号3',blank=True)
    non_routine_note_number_4 = models.CharField(max_length=10, verbose_name=u'非例行收费单编号4',blank=True)
    non_routine_note_number_5 = models.CharField(max_length=10, verbose_name=u'非例行收费单编号5',blank=True)
    description = models.TextField(verbose_name = u'工作描述', blank= True)
    man_hour = models.DecimalField(max_digits=4, decimal_places=1,verbose_name = u'工时')
    hangar_time_range = models.TextField(verbose_name=u'机库使用时间范围', blank=True)
    hanger_hour = models.BigIntegerField(verbose_name=u'机库使用小时数', blank=True, null=True)
    runup_ramp_time_range = models.TextField(verbose_name=u'试车坪使用时间范围', blank=True)
    runup_ramp_big_25_time = models.BigIntegerField(verbose_name=u'试车坪（2.5万磅以上）使用小时数', blank=True, null=True)
    runup_ramp_small_25_time = models.BigIntegerField(verbose_name=u'试车坪（2.5万磅以下）使用小时数', blank=True, null=True)
    gpu = models.BigIntegerField(verbose_name=u'地面电源', blank=True, null=True)
    transfer = models.BigIntegerField(verbose_name=u'转接车', blank=True, null=True)
    ground_power_unit = models.BigIntegerField(verbose_name=u'电源车', blank=True, null=True)
    tow_tug = models.BigIntegerField(verbose_name=u'拖车', blank=True, null=True)
    towbar = models.BigIntegerField(verbose_name=u'拖把', blank=True, null=True)
    towing_push_tractor = models.BigIntegerField(verbose_name=u'牵引车', blank=True, null=True)
    seat_elevating_truck = models.BigIntegerField(verbose_name=u'座椅升降平台车', blank=True, null=True)
    forklift = models.BigIntegerField(verbose_name=u'叉车', blank=True, null=True)
    air_conditioning = models.BigIntegerField(verbose_name=u'空调车', blank=True, null=True)
    pallet_jack = models.BigIntegerField(verbose_name=u'液压车', blank=True, null=True)
    truck = models.BigIntegerField(verbose_name=u'内场运输车', blank=True, null=True)
    ndt = models.BigIntegerField(verbose_name=u'NDT 设备', blank=True, null=True)
    air_starter = models.BigIntegerField(verbose_name=u'气源车', blank=True, null=True)
    lifting_platform_truck = models.BigIntegerField(verbose_name=u'升降工作平台车', blank=True, null=True)
    small_tow_cart = models.BigIntegerField(verbose_name=u'小拖车', blank=True, null=True)
    cherry_picker = models.BigIntegerField(verbose_name=u'梯子车', blank=True, null=True)
    platform = models.BigIntegerField(verbose_name=u'工作梯', blank=True, null=True)
    jack = models.BigIntegerField(verbose_name=u'千斤顶', blank=True, null=True)
    borescope = models.BigIntegerField(verbose_name=u'孔探（不含人工）', blank=True, null=True)
    generator_and_light_source = models.BigIntegerField(verbose_name=u'孔探发电机及光源', blank=True, null=True)
    oil_service_cart = models.BigIntegerField(verbose_name=u'滑油加油车', blank=True, null=True)
    high_cherry_picker = models.BigIntegerField(verbose_name=u'高空车', blank=True, null=True)
    oil = models.DecimalField(max_digits=4, decimal_places=1,verbose_name = u'滑油（夸脱）', blank= True, null=True)
    hydraulic = models.DecimalField(max_digits=4, decimal_places=1,verbose_name = u'液压油（加仑）', blank= True, null=True)
    deicing_fluid = models.DecimalField(max_digits=4, decimal_places=1,verbose_name = u'除冰液（公斤）', blank= True, null=True)


    class Meta:
        verbose_name_plural = u'收费单'

    def __unicode__(self):
        return u'%s %s' % (self.date, self.ac_number)


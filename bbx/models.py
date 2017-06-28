#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class bbx_info(models.Model):
    company = models.CharField(max_length=2, verbose_name=u'公司')
    filiale = models.CharField(max_length=20, verbose_name=u'分公司', blank=True)
    category = models.CharField(max_length=10, verbose_name=u'类别')
    date = models.DateField(u'日期')
    arrival_flight_number = models.CharField(max_length=5, verbose_name=u'进港航班', blank= True)
    depart_flight_number = models.CharField(max_length=5, verbose_name=u'离港航班', blank= True)
    ac_type = models.CharField(max_length=10, verbose_name=u'机型')
    ac_number = models.CharField(max_length=4, verbose_name=u'机号')
    sector_number = models.CharField(max_length=10, verbose_name=u'航段编号')
    note_number_1 = models.CharField(max_length=10, verbose_name=u'收费单编号1',blank=True)
    note_number_2 = models.CharField(max_length=10, verbose_name=u'收费单编号2',blank=True)
    note_number_3 = models.CharField(max_length=10, verbose_name=u'收费单编号3',blank=True)
    description = models.TextField(verbose_name = u'问题描述', blank= True)
    man_hour = models.DecimalField(max_digits=4, decimal_places=1,verbose_name = u'工时', blank= True)
    ground_equipment = models.TextField(verbose_name=u'地面设备', blank=True)
    oil = models.DecimalField(max_digits=4, decimal_places=1,verbose_name = u'滑油', blank= True)
    hydraulic = models.DecimalField(max_digits=4, decimal_places=1,verbose_name = u'液压油', blank= True)
    deicing_fluid = models.DecimalField(max_digits=4, decimal_places=1,verbose_name = u'除冰液', blank= True)


    class Meta:
        verbose_name_plural = u'收费单'

    def __unicode__(self):
        return u'%s %s' % (self.date, self.ac_number)


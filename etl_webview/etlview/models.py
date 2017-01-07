from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SerInData(models.Model):
  hourly_date = models.DateTimeField()
  display_date = models.CharField(max_length=200)
  co_cop = models.CharField(max_length=200)
  co_tg = models.CharField(max_length=200)
  o3_cop = models.CharField(max_length=200)
  o3_tg = models.CharField(max_length=200)
  no2_cop = models.CharField(max_length=200)
  no2_tg = models.CharField(max_length=200)
  c6h6_cop = models.CharField(max_length=200)
  c6h6_tg = models.CharField(max_length=200)
  temp_cop = models.CharField(max_length=200)
  temp_tg = models.CharField(max_length=200)
  rh_cop = models.CharField(max_length=200)
  rh_tg = models.CharField(max_length=200)
  noise_cop = models.CharField(max_length=200)
  noise_tg = models.CharField(max_length=200)
  tab08_cop = models.CharField(max_length=200)
  tab08_tg = models.CharField(max_length=200)
  tab09_cop = models.CharField(max_length=200)
  tab09_tg = models.CharField(max_length=200)
  tab10_cop = models.CharField(max_length=200)
  tab10_tg = models.CharField(max_length=200)
  def __str__(self):
    return self.hourly_date
  

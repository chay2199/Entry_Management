from django.core.validators import RegexValidator
from django.db import models


class CheckIn(models.Model):
    visitor_name = models.CharField(max_length=200, null=True)
    visitor_email = models.EmailField(max_length=254, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the"
                                         " format: '+999999999'. Up to 15 digits allowed.")
    visitor_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    host_name = models.CharField(max_length=200, null=True)
    host_email = models.EmailField(max_length=254, null=True)
    host_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    checkTime = models.TimeField(auto_now=False)

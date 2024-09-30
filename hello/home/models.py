from django.db import models

# Create your models here.

class Company(models.Model):
    CONDITION = (('Active', 'Active'),('Deactivate','Deactivate'))
    companyname = models.CharField(max_length=255)
    companyid = models.CharField(max_length=20, unique=True)
    contactperson_name = models.CharField(max_length=100)
    contactemail = models.EmailField()
    contactphonenumber = models.CharField(max_length=20)
    companyaddressstreet = models.CharField(max_length=255)
    companyaddresscity = models.CharField(max_length=100)
    companyaddressstate = models.CharField(max_length=100)
    companyaddresspostalcode = models.CharField(max_length=20)
    companyaddresscountry = models.CharField(max_length=100)
    companytype = models.CharField(max_length=50)
    companyregistrationnumber = models.CharField(max_length=50, blank=True, null=True)
    companytaxidentificationnumber = models.CharField(max_length=50, blank=True, null=True)
    companyindustrytype = models.CharField(max_length=100)
    companydateofestablishment = models.DateField()
    companynumberofemployees = models.IntegerField()
    companybusinesshours = models.CharField(max_length=100)
    companywebsiteurl = models.URLField(blank=True, null=True)
    companyfacebookurl = models.URLField(blank=True, null=True)
    companytwitterurl = models.URLField(blank=True, null=True)
    companylinkedinurl = models.URLField(blank=True, null=True)
    companyinstagramurl = models.URLField(blank=True, null=True)
    companylogoimage = models.ImageField(upload_to='shop/images', blank=True, null=True)
    companyadditionalnotes = models.TextField(blank=True)
    condition = condition = models.CharField(choices=CONDITION,max_length=200) 

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.companyname


    








from django.db import models
from django.contrib.auth.models import AbstractUser


class customuser(AbstractUser):
    usertype=[
        ('recruiter','Recruiter'),
        ('job_seeker','Job_Seeker'),
    ]
    
    usertype=models.CharField(choices=usertype,max_length=100, null=True)
    display_name=models.CharField(max_length=100, null=True)


    
    # Basic Information
    # Father_name=models.CharField(max_length=100,null=True)
    # Mother_name=models.CharField(max_length=100,null=True)
    
    # Contact
    # phone=models.CharField(max_length=100,null=True)
    # emergency_contact=models.CharField(max_length=100,null=True)
    
    # education_qualification=models.CharField(max_length=100, null=True)
    # work_experience=models.CharField(max_length=100, null=True)
    
class jobmodel(models.Model):
    title=models.CharField(max_length=100, null=True)
    numberOfOpenings=models.CharField(max_length=100, null=True)
    category=models.ImageField(upload_to='Picture', null=True)
    jobDescription=models.CharField(max_length=100, null=True)
    skill=models.CharField(max_length=100, null=True)
    
    
    created_by=models.ForeignKey(customuser, on_delete=models.CASCADE, null=True)
    


class JobApplyModel(models.Model):
    apply_by=models.ForeignKey(customuser,on_delete=models.CASCADE, null=True)
    apply_to=models.ForeignKey(jobmodel,on_delete=models.CASCADE, null=True)
    resume=models.FileField(upload_to='resume',null=True)


class recruiterprofile(models.Model):
    user = models.ForeignKey(customuser,on_delete=models.CASCADE, null=True,)
    company_name = models.CharField(max_length=100, null=True)


class seekerprofile(models.Model):
    user = models.ForeignKey(customuser,on_delete=models.CASCADE, null=True)
    skill = models.CharField(max_length=100, null=True)
    resume=models.FileField(upload_to='resume',null=True)
    
    
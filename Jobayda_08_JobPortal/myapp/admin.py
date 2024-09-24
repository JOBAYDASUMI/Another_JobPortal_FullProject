from django.contrib import admin
from .models import *

admin.site.register(customuser)
admin.site.register(jobmodel)
admin.site.register(JobApplyModel)
admin.site.register(recruiterprofile)
admin.site.register(seekerprofile)
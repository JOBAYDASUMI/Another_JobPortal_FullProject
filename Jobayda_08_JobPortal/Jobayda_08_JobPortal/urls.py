from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Hannan_08_JobPortal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',signin,name='signin'),
    path('signup/',signup,name='signup'),
    path('signout/',signout,name='signout'),
    path('index/',index,name='index'),
    path('dashboard/',dashboard,name='dashboard'),
    path('searchpage/',searchpage,name='searchpage'),
    
    
    path('addjob/',addjob,name='addjob'),
    path('updatejob/',updatejob,name='updatejob'),
    path('editjob/<str:myid>',editjob,name='editjob'),
    path('deletejob/<str:myid>',deletejob,name='deletejob'),
    path('jobdetails/<str:myid>',jobdetails,name='jobdetails'),
    path('joblistforall/',joblistforall,name='joblistforall'),
    path('joblistforrecruiter/',joblistforrecruiter,name='joblistforrecruiter'),
    
    
    
    path('applyjob/<str:myid>',applyjob,name='applyjob'),
    path('appliedjob/',appliedjob,name='appliedjob'),
    # path('viewapplicant/<str:myid>',viewapplicant,name='viewapplicant'),
    
    path('profile/',profile,name="profile"),
    path('updateprofile/',updateprofile,name='updateprofile'),
    path('editprofile/',editprofile,name='editprofile'),
    path('changepassword/',changepassword,name="changepassword"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

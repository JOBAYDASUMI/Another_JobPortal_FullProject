from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q



def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect("dashboard")
        
    return render(request,'signin.html')




def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        display_name=request.POST.get('display_name')
        email=request.POST.get('email')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        usertype=request.POST.get('usertype')
        if password == confirm_password:
            user_creation=customuser.objects.create_user(username=username, password=password)
            user_creation.display_name=display_name
            user_creation.email=email
            user_creation.usertype=usertype
            user_creation.save()
            return redirect("signin")
    return render(request,'signup.html')


def signout(request):
    logout(request)
    return redirect("signin")

@login_required
def dashboard(request):
    myjobs=jobmodel.objects.all()
    job_filtered=[]
    for i in myjobs:
        already_applied=JobApplyModel.objects.filter(apply_by=request.user,apply_to=i).exists()
        job_filtered.append(
            (i,already_applied),
        )
    myDict={
        'myjob':job_filtered
    }
    return render(request,'dashboard.html',myDict)

@login_required
def index(request):
    return render(request,'index.html')



@login_required
def addjob(request):
    current_user=request.user
    if request.method == 'POST':
        title=request.POST.get('title')
        numberOfOpenings=request.POST.get('numberOfOpenings')
        category=request.POST.get('category')
        jobDescription=request.POST.get('jobDescription')
        skill=request.POST.get('skill')

        myjob=jobmodel(
            title=title,
            numberOfOpenings=numberOfOpenings,
            category=category,
            jobDescription=jobDescription,
            skill=skill,
        )
        myjob.created_by=current_user
        myjob.save()
        return redirect("joblistforall")
    return render(request,'addjob.html')



@login_required
def joblistforall(request):
    myjobs=jobmodel.objects.all()
    job_filtered=[]
    for i in myjobs:
        already_applied=JobApplyModel.objects.filter(apply_by=request.user,apply_to=i).exists()
        job_filtered.append(
            (i,already_applied),
        )
    myDict={
        'myjob':job_filtered
    }
    return render(request,'joblistforall.html',myDict)


@login_required
def joblistforrecruiter(request):
    current_user=request.user
    myjob=jobmodel.objects.filter(created_by=current_user)
    myDict={
        'myjob':myjob
    }
    return render(request,'joblistforrecruiter.html',myDict)

@login_required
def editjob(request,myid):
    myjob=jobmodel.objects.filter(id=myid)
    myDict={
        'myjob':myjob
    }
    return render(request,'editjob.html',myDict)



@login_required
def updatejob(request):
    current_user=request.user
    if request.method == 'POST':
        id=request.POST.get('id')
        title=request.POST.get('title')
        numberOfOpenings=request.POST.get('numberOfOpenings')
        
        category=request.POST.get('category')
        jobDescription=request.POST.get('jobDescription')
        skill=request.POST.get('skill')
        
        myjob=jobmodel(
            id=id,
            title=title,
            numberOfOpenings=numberOfOpenings,
            
            category=category,
            jobDescription=jobDescription,
            skill=skill,
        )
            
        myjob.created_by=current_user
        myjob.save()
        return redirect("joblistforrecruiter")
    
@login_required
def deletejob(request,myid):
    myjob=jobmodel.objects.get(id=myid)
    myjob.delete()
    return redirect("joblistforrecruiter")
    



@login_required
def jobdetails(request,myid):
    myjob=jobmodel.objects.filter(id=myid)
    myDict={
        'myjob':myjob
    }
    return render(request,'jobdetails.html',myDict)



@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def changepassword(request):
    current_user = request.user
    if request.method == 'POST':
        oldpassword = request.POST.get('oldpassword')
        newpassword = request.POST.get('newpassword')
        confirmnewpassword = request.POST.get('confirmnewpassword')
        if newpassword == confirmnewpassword:
            if check_password(oldpassword, current_user.password):
                current_user.set_password(newpassword)
                update_session_auth_hash(request,current_user)
                current_user.save()
                return redirect('profile')
    return render(request,'changepassword.html')

@login_required
def searchpage(request):
    query = request.GET.get('search')
    search = jobmodel.objects.filter(
        Q(title__icontains=query) | 
        Q(jobDescription__icontains=query) |
        Q(skill__icontains=query)
    )
    myDict = {
        'search': search,
        'query':query
    }
    return render(request,'searchpage.html',myDict)



@login_required
def applyjob(request,myid):
    myjob = get_object_or_404(jobmodel, id =myid)
    current_user = request.user
    if request.method == 'POST':
        resume = request.FILES.get('resume')
        
        application = JobApplyModel.objects.create(
            apply_by = current_user,
            apply_to = myjob,
            resume = resume,
        )
        application.save()
    return render(request,'applyjob.html',{'myjob':myjob})


@login_required
def appliedjob(request):
    appliedjob = JobApplyModel.objects.all()
    myDict = {
        'appliedjob':appliedjob
    }
    return render(request,'appliedjob.html',myDict)


# @login_required
# def viewapplicant(request,myid):
#     myjob = jobmodel.objects.get(id = myid)
#     applicants = JobApplyModel.objects.filter(apply_to = myjob)
#     myDict = {
#         'myjob':myjob,
#         'applicants':applicants,
#     }
#     return render(request,'viewapplicant.html',myDict)

@login_required
def editprofile(request):
    myjob=jobmodel.objects.filter()
    myDict={
        'myjob':myjob
    }
    return render(request,'editprofile.html',myDict)


@login_required
def updateprofile(request):
    current_user=request.user
    if request.method == 'POST':
        id=request.POST.get('id')
        username=request.POST.get('username')
        skill=request.POST.get('skill')
        
        myjob=recruiterprofile(
            id=id,
            username=username,
            skill=skill,
            
        )
            
        myjob.created_by=current_user
        myjob.save()
        return redirect("profile")
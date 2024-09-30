from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import get_object_or_404 
# from django.urls import reverse
from home.models import Company
from django.contrib import messages
from .forms import CompanyForm
# Create your views here.
def home(request):
    
    return render(request , 'home.html')
def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =  authenticate(username = username , password = password)
        
        if user is not None:
            login(request,user)
            return redirect('home.html')
        else:
            return redirect('home.html')
        
    return render(request , 'login.html')
def logoutuser(request):
    logout(request)
    return render(request , 'logout.html')
def companydata(request):
    HttpResponse("Welcome to the Companu Add Data")   
    emps = Company.objects.all()
    
    context = {
        'emps' : emps
    } 
    return render(request , 'companydata.html' , context)
def userdata(request):
    return render(request , 'userdata.html')
def companyedit(request , company_id):
    company = get_object_or_404(Company, id=company_id)
    
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')  # Redirect to a view displaying all companies (adjust as needed)
    else:
        form = CompanyForm(instance=company)
    
    context = {
        'form': form,
        'company': company,
    }
    return render(request, 'companyedit.html' , context)

def companyadd(request):
    HttpResponse("Welcome to the Company Add")    
    if request.method == "POST":
        companyname = request.POST.get('companyname')
        companyid = request.POST.get('companyid')
        contactperson_name = request.POST.get('contactperson_name')
        contactemail = request.POST.get('contactemail')
        contactphonenumber = request.POST.get('contactphonenumber')
        companyaddressstreet = request.POST.get('companyaddressstreet')
        companyaddresscity = request.POST.get('companyaddresscity')
        companyaddressstate = request.POST.get('companyaddressstate')
        companyaddresspostalcode = request.POST.get('companyaddresspostalcode')
        companyaddresscountry = request.POST.get('companyaddresscountry')
        companytype = request.POST.get('companytype')
        companyregistrationnumber = request.POST.get('companyregistrationnumber')
        companytaxidentificationnumber = request.POST.get('companytaxidentificationnumber')
        companyindustrytype = request.POST.get('companyindustrytype')
        companydateofestablishment = request.POST.get('companydateofestablishment')
        companynumberofemployees = request.POST.get('companynumberofemployees')
        companybusinesshours = request.POST.get('companybusinesshours')
        companywebsiteurl = request.POST.get('companywebsiteurl')
        companyfacebookurl = request.POST.get('companyfacebookurl')
        companytwitterurl = request.POST.get('companytwitterurl')
        companylinkedinurl = request.POST.get('companylinkedinurl')
        companyinstagramurl = request.POST.get('companyinstagramurl')
        companylogoimage = request.FILES.get('companylogoimage')
        companyadditionalnotes = request.POST.get('companyadditionalnotes')
        companydata = Company(companyname = companyname , companyid = companyid , contactperson_name = contactperson_name , contactemail = contactemail
                               , contactphonenumber = contactphonenumber , companyaddressstreet = companyaddressstreet , companyaddresscity = companyaddresscity ,
                               companyaddressstate = companyaddressstate , companyaddresspostalcode = companyaddresspostalcode,
                               companyaddresscountry = companyaddresscountry , companytype = companytype , companyregistrationnumber = companyregistrationnumber ,
                               companytaxidentificationnumber = companytaxidentificationnumber , companyindustrytype = companyindustrytype , companydateofestablishment = companydateofestablishment ,
                               companynumberofemployees = companynumberofemployees , companybusinesshours = companybusinesshours , companywebsiteurl = companywebsiteurl ,
                               companyfacebookurl = companyfacebookurl , companytwitterurl = companytwitterurl , companylinkedinurl = companylinkedinurl , companyinstagramurl = companyinstagramurl ,
                               companylogoimage = companylogoimage , companyadditionalnotes = companyadditionalnotes)
        
        companydata.save()
        messages.success(request, "Thank You!")
    return render(request , 'companyadd.html')
def companysearch(request):
    quary = request.GET.get('quary')
    emps = Company.objects.filter(companyname__icontains=quary)  # Adjust field name here

    context = {
        'emps': emps,
    }
    return render(request, 'companysearch.html', context)

def companyactive(request , company_id):
    return render(request , 'companyactive.html')
       
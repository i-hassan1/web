from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'security_website/index.html')

def services(request):
	return render(request, 'security_website/services.html')

def contact_us(request):
	return render(request, 'security_website/contact_us.html')

def solutions(request):
	return render(request, 'security_website/solutions.html')

def customers(request):
	return render(request, 'security_website/customers.html')

def blog(request):
	return render(request, 'security_website/blog.html')

def redteam(request):
	return render(request, 'security_website/redteam.html')

def vulnerability_assessment (request):
	return render(request, 'security_website/vulnerability_assessment.html')

def cloud_security(request):
	return render(request, 'security_website/cloud_security.html')

def source_code_analysis(request):
	return render(request, 'security_website/source_code_analysis.html')

def govt(request):
	return render(request, 'security_website/govt.html')

def retail(request):
	return render(request, 'security_website/retail.html')

def finance(request):
	return render(request, 'security_website/finance.html')

def health(request):
	return render(request, 'security_website/health.html')

def education(request):
	return render(request, 'security_website/education.html')

def telecom(request):
	return render(request, 'security_website/telecom.html')

def Insurance(request):
	return render(request, 'security_website/Insurance.html')

def Startups(request):
	return render(request, 'security_website/Startups.html')

def EnterpriseNetworks(request):
	return render(request, 'security_website/EnterpriseNetworks.html')
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='security_website-home'),
    path('home/', views.home, name='security_website-home'),
    path('services/', views.services, name='security_website-services'),
    path('contact_us/', views.contact_us, name='security_website-contactus'),
    path('solutions/', views.solutions, name='security_website-solutions'),
    path('customers/', views.customers, name='security_website-customers'),
    path('blog/', views.blog, name='security_website-blog'),
    path('redteam/', views.redteam, name='security_website-redteam'),
    path('vulnerability_assessment/', views.vulnerability_assessment, name='security_website-vulnerability_assessment'),
    path('cloud_security/', views.cloud_security, name='security_website-cloud_security'),
    path('source_code_analysis/', views.source_code_analysis, name='security_website-source_code_analysis'),
    path('govt/', views.govt, name='security_website-govt'),
    path('retail/', views.retail, name='security_website-retail'),
    path('finance/', views.finance, name='security_website-finance'),
    path('health/', views.health, name='security_website-health'),
    path('education/', views.education, name='security_website-education'),
    path('telecom/', views.telecom, name='security_website-telecom'),
    path('Insurance/', views.Insurance, name='security_website-Insurance'),
    path('Startups/', views.Startups, name='security_website-Startups'),
    path('EnterpriseNetworks/', views.EnterpriseNetworks, name='security_website-EnterpriseNetworks'),


]

from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.home , name = 'home.html'),
    path('login.html', views.loginuser , name = 'login.html'),
    path('logout.html', views.logoutuser , name = 'logout.html'),
    path('companydata.html', views.companydata , name = 'companydata.html'),
    path('userdata.html', views.userdata , name = 'userdata.html'),
    path('companyedit/<int:company_id>', views.companyedit , name = 'companyedit.html'),
    path('companyadd.html', views.companyadd , name = 'companyadd.html'),
    path('companysearch.html/', views.companysearch, name='company_search'),
    path('companyactive/<int:company_id>', views.companyactive , name = 'companyactive.html'),
] 

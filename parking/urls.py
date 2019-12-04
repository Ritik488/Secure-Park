from django.urls import path
from .import views


urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('park1/', views.park1, name='park1'),
    path('entryexit/', views.entryexit, name='entryexit'),
    path('signup/', views.signup, name='signup'),
    path('entry/', views.entry, name='entry'),
    path('forgot/', views.forgot, name='forgot'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('fare/', views.fare, name='fare'),
    path('maps/', views.maps, name='maps'),
    path('contactus/',views.contactus, name='contactus'),
    path('details/', views.details, name='details'),
    path('complaint/', views.complaint, name='complaint'),
    path('exit/',views.exit, name='exit'),
    path('exitdetails/', views.exitdetails, name='exitdetails'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('printcontact/',views.printcontact, name='printcontact'),
    path('printcomplaint/', views.printcomplaint, name='printcomplaint'),
    path('printvehicles/', views.printvehicles, name='printvehicles'),
]
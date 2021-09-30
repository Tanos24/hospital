from main.forms import AddDoctor, AddNurses, AddPatients
from django.urls import path
from .views import detail, index, AddDoctors,AddNurse,AddPatient,register,signin,signout


urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', detail, name='detail'),
    path('doctor/registration',AddDoctors.as_view(),name='adddoctor'),
    path('nurse/registration',AddNurse.as_view(),name='addnurse'),
    path('patient/registration',AddPatient.as_view(),name='addpatients'),
    path('register/',register,name='register'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout')
]
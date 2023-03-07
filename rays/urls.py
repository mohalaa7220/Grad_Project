
from django.urls import path
from .views import AddDoctorRays, PatientRays

urlpatterns = [
    path('add', AddDoctorRays.as_view(), name='add_rays'),
    path('', AddDoctorRays.as_view(), name='get_rays'),
    path('patient_rays/<str:pk>', PatientRays.as_view(), name='patient_rays'),
]

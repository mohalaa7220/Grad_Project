from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework import status
from .models import Rays, Doctor, Nurse, Patient
from .serializer import (DoctorRaysSerializer, ResultDoctorRaysSerializer)
from rest_framework.permissions import IsAuthenticated
from notifications.signals import notify
from api.models import User
# ====================== Doctor =======================================


class AddDoctorRays(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorRaysSerializer

    def post(self, serializer):
        data = self.request.data
        doctor = Doctor.objects.get(user=self.request.user)
        serializer = self.serializer_class(data=data)
        nurses = data.get('nurse')
        nurse_instance = User.objects.filter(id__in=nurses)

        if serializer.is_valid(raise_exception=True):
            result = serializer.save(doctor=doctor)
            notify.send(sender=doctor, recipient=nurse_instance,
                        verb='you reached level 10')
            response = {
                "ray": ResultDoctorRaysSerializer(result, context=self.get_serializer_context()).data,
                "message": "Rays Added successfully",
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

    def get(self, request):
        user = request.user
        current_doctor = Doctor.objects.get(user=user)
        report = current_doctor.doctor_rays.all()
        serializer = ResultDoctorRaysSerializer(report, many=True)

        return Response({"result": report.count(), 'rays': serializer.data})


# ====================== Nurse =======================================
class PatientRays(generics.ListCreateAPIView):
    def get(self, request, pk=None):
        patient = Patient.objects.get(pk=pk)
        rays = patient.patient_rays.all()
        print(rays)
        return Response({''}, status=status.HTTP_200_OK)

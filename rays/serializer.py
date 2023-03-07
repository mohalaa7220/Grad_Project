from rest_framework import serializers
from .models import Rays, Nurse


class DoctorRaysSerializer(serializers.ModelSerializer):
    nurse = serializers.SlugRelatedField(
        slug_field="user_id", queryset=Nurse.objects.all(), many=True)

    class Meta:
        model = Rays
        fields = ['name', 'nurse', 'patient']


class ResultDoctorRaysSerializer(serializers.ModelSerializer):
    nurse = serializers.SerializerMethodField(source='get_nurse')
    patient = serializers.StringRelatedField()

    class Meta:
        model = Rays
        fields = ['id', 'name', 'nurse', 'patient', 'created', 'updated']

    # ========= Get Nurse Information
    @staticmethod
    def get_nurse(obj):
        nurse_list = []
        nurse = obj.nurse.all()
        for i in nurse:
            data = i.user
            nurse_list.append({"name": data.name})
        return nurse_list

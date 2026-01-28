from rest_framework import serializers # type: ignore
from api_work.models import *
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields = "__all__"

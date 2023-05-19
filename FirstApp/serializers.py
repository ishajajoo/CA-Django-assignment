from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student #attribute to class
        fields = ['name', 'id', 'contact', 'address']
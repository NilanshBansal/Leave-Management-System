from rest_framework import serializers
from .models import Executive, Manager, ExecLeaveRequest, LeaveBalance
from django.contrib.auth.hashers import make_password

class ExecutiveSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    
    class Meta:
        model = Executive
        fields = ('url','Exec_No','First_Name','Last_Name','password','Birth_Date','Address','Mobile_Number','Email_Address','Hire_Date','Man_ID')

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = Manager
        fields = ('url','Man_No','First_Name','Last_Name','password','Birth_Date','Address','Mobile_Number','Email_Address','Hire_Date')

class ExecLeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecLeaveRequest
        fields = '__all__'

class LeaveBalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LeaveBalance
        fields = '__all__'
from rest_framework import serializers
from .models import Executive, Manager, ExecLeaveRequest, LeaveBalance

class ExecutiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Executive
        fields = '__all__'

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class ExecLeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecLeaveRequest
        fields = '__all__'

class LeaveBalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LeaveBalance
        fields = '__all__'
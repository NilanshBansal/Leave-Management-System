from django.shortcuts import render
from .serializers import ExecutiveSerializer, ManagerSerializer, ExecLeaveRequestSerializer, LeaveBalanceSerializer
from rest_framework import viewsets, permissions
from .models import Executive, Manager, ExecLeaveRequest, LeaveBalance

class ExecutiveViewSet(viewsets.ModelViewSet):
    serializer_class = ExecutiveSerializer
    queryset = Executive.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

class ManagerViewSet(viewsets.ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

class ExecLeaveRequestViewSet(viewsets.ModelViewSet):
    serializer_class = ExecLeaveRequestSerializer
    queryset = ExecLeaveRequest.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

class LeaveBalanceViewSet(viewsets.ModelViewSet):
    serializer_class = LeaveBalanceSerializer
    queryset = LeaveBalance.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
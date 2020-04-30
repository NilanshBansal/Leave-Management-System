from django.shortcuts import render
from .serializers import ExecutiveSerializer, ManagerSerializer, ExecLeaveRequestSerializer, LeaveBalanceSerializer
from rest_framework import viewsets, permissions
from .models import Executive, Manager, ExecLeaveRequest, LeaveBalance
from rest_framework import permissions

class ExecutiveViewSet(viewsets.ModelViewSet):
    serializer_class = ExecutiveSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Executive.objects.all()
        return Executive.objects.filter(Man_ID__Email_Address=user)
    permission_classes = (permissions.IsAuthenticated,)

class ManagerViewSet(viewsets.ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()
    permission_classes = (permissions.IsAdminUser,permissions.IsAuthenticated,)

class ExecLeaveRequestViewSet(viewsets.ModelViewSet):
    serializer_class = ExecLeaveRequestSerializer
    queryset = ExecLeaveRequest.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class LeaveBalanceViewSet(viewsets.ModelViewSet):
    serializer_class = LeaveBalanceSerializer
    queryset = LeaveBalance.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
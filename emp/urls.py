from rest_framework import routers
from .views import ExecutiveViewSet, ManagerViewSet, ExecLeaveRequestViewSet, LeaveBalanceViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('executive', ExecutiveViewSet, base_name='executive')
router.register('manager', ManagerViewSet, base_name='manager')
router.register('execleave', ExecLeaveRequestViewSet, base_name='execleave')
router.register('leavebalance', LeaveBalanceViewSet, base_name='leavebalance')

urlpatterns = [
    path('', include(router.urls)),
]

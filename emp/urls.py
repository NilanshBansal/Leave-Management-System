from rest_framework import routers
from .views import ExecutiveViewSet, ManagerViewSet, ExecLeaveRequestViewSet, LeaveBalanceViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('executive', ExecutiveViewSet)
router.register('manager', ManagerViewSet)
router.register('execleave', ExecLeaveRequestViewSet)
router.register('leavebalance', LeaveBalanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

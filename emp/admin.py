from django.contrib import admin
from .models import *
# Register your models here.
models = [Manager,Executive,ExecLeaveRequest,LeaveBalance]
admin.site.register(models)

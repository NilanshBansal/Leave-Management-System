from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



LEAVE_TYPES =(
    ('PL', 'Personal Leave'),
    ('AL', 'Annual Leave'),
    ('OT','Other')
)

LEAVE_STATUS =(
    ('PE', 'Pending'),
    ('AP', 'Approved'),
    ('DL','Declined'),
    ('CA','Cancelled')
)

class Manager(models.Model):
    Man_No = models.AutoField(primary_key=True,help_text='Unique Man no for Manager table')
    First_Name = models.CharField(max_length=14,help_text='Manager first name')
    Last_Name = models.CharField(max_length=14,help_text='Manager last name',blank=True, null=True)
    password = models.CharField(max_length=200, null=True)
    Birth_Date = models.DateField(help_text='Manager birth date',blank=True, null=True)
    Address = models.CharField(max_length=300, blank=True, null=True)
    Mobile_Number = models.PositiveIntegerField(default=0)
    Email_Address = models.EmailField(max_length=80, unique=True)
    Hire_Date = models.DateField(help_text='Manager joining date')
    def __str__(self):
        return '%s %s %s' % (self.Man_No, self.First_Name, self.Last_Name)

class Executive(models.Model):
    Exec_No = models.AutoField(primary_key=True,help_text='Unique Exec no for Executive table')
    First_Name = models.CharField(max_length=14,help_text='Executive first name')
    Last_Name = models.CharField(max_length=14,help_text='Executive last name',blank=True, null=True)
    password = models.CharField(max_length=200, null=True)
    Birth_Date = models.DateField(help_text='Executive birth date',blank=True, null=True)
    Address = models.CharField(max_length=300, blank=True, null=True)
    Mobile_Number = models.PositiveIntegerField(default=0)
    Email_Address = models.EmailField(max_length=80, unique=True)
    Hire_Date = models.DateField(help_text='Executive joining date')
    Man_ID = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name="Man_ID", default=0)
    def __str__(self):
        return '%s %s %s' % (self.Exec_No, self.First_Name, self.Last_Name)

class ExecLeaveRequest(models.Model):
    ExecLeave_Req_ID = models.AutoField(primary_key=True)
    Exec_ID = models.ForeignKey(Executive, on_delete=models.CASCADE, related_name="Exec_ID", default=0)
    Leave_Type = models.CharField(max_length=30, choices=LEAVE_TYPES)
    Man_ID = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name="Manager_Emp_No", default=0)
    Begin_Date = models.DateField(help_text='Leave begin date')
    End_Date = models.DateField(help_text='Leave end date')
    Requested_Days = models.PositiveIntegerField(default=0,help_text='Total no of requested leave days')
    Leave_Status = models.CharField(max_length=10, choices=LEAVE_STATUS)
    Exec_Comments = models.CharField(max_length=500, null=True)

    def __str__(self):
        return '%s %s' % (self.ExecLeave_Req_ID, self.Exec_ID)


class LeaveBalance(models.Model):

    LeaveBal_ID = models.AutoField(primary_key=True)
    Exec_ID = models.ForeignKey(Executive, on_delete=models.CASCADE)
    Leave_Type = models.CharField(max_length=10, choices=LEAVE_TYPES)
    Available_Days = models.PositiveIntegerField(default=0, help_text='Remaining/available leave days per executive')
    Allocated_Days = models.PositiveIntegerField(default=0, help_text='No of leave days allocated to a leave type per '
                                                                      'executive per year')

    def __str__(self):
        return '%s %s' % (self.Exec_ID, self.Leave_Type)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        User.objects.create_user(username=kwargs['instance'].First_Name, password=kwargs['instance'].password)

post_save.connect(create_profile, sender=Executive)

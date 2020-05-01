# Leave-Management-System
 
### Setup on Local machine

- virtualenv leaveenv --python=python3
- source leaveenv/bin/activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

### You can use it at https://lms-nilansh.herokuapp.com/

### Superuser details
Username: nilansh
Email: bansalnilansh@gmail.com
Password: Hello@123

### WorkFlow:

1. Superuser can create or remove any Manager and Executive.
2. Manager can add an executive. Manager can only remove an Executive added by him. 
3. Executive requests for leave and selects for the manager to approve. 
4. Manager can only view and change the status of the requests which are raised to him. 
5. Executive can only view and edit the requests raised by him.
6. Executive cannot add or remove other executives.
7. Manager cannot add or remove other managers.

from django.shortcuts import render, HttpResponse
from database_modelling.models import Employee, Department, Project
# Create your views here.


def RelationshipView(request, *args, **kwargs):
    # creating Department database.
    hr = Department.objects.create(name='HR')
    accounts = Department.objects.create(name='Accounts')
    software = Department.objects.create(name='Software')

    # creating Employee database.
    e1 = Employee.objects.create(name='John', age='30', department=hr)
    e2 = Employee.objects.create(name='Jonny', age='30', department=accounts)
    e3 = Employee.objects.create(name='Jen', age='30', department=software)

    # performing operations.(one to many)
    get_emp_dept = Employee.objects.get(name='John').department.name
    emp_in_dept = Employee.objects.filter(department__name='Software')
    all_emp_in_a_dept = Employee.objects.filter(department=hr)
    emp_age = Department.objects.all().filter(employees__age__gt=25)

    # performing operations.(many to many).
    project1 = Project.objects.create(title='first_project')
    project2 = Project.objects.create(title='second_project')

    project1.employee.add(e1, e2)
    project2.employee.add(e1, e2)
    project2.employee.add(e3)

    # project objects have access to their related employee objects.
    project1.employee.all()

    # employee objects have access to their related project objects.
    e1.project_set.all()
    e3.project_set.all()

    # operations.
    Project.objects.filter(employee__id=1)
    Project.objects.filter(employee=e1)
    Project.objects.filter(employee__name__startswith='Jen')

    Employee.objects.filter(id=1)
    Employee.objects.filter(project__id=1)

    # project to an employee can also be added this way.(other end).
    e1.project_set.add(project2)

    # by this we can remove an employee from a project.
    project1.employee.remove(e1)

    # from other end.
    e2.project_set.remove(project1)

    # clear relation set.
    e1.project_set.clear()
    project1.employee.clear()

    return HttpResponse("Successful")

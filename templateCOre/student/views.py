from django.shortcuts import render

# ! Create your views here.

def allStudent(request):
    myvars = {'fname':'Muhammedx',
            'lname':'ESSA',
            'mylist':[1, 2, 3, 4, 5, 6, 7, 8],
            'mydict':{'python':'django'},
            
            }
    return render(request, 'student.html', context=myvars)

def addStudent(request):
    return render(request, 'add.html')

def editStudent(request):
    return render(request, 'edit.html')
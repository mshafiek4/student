from django.shortcuts import render,redirect,HttpResponse

from .models import Student, Classes, Professor

# Create your views here.


def home(request):
    students = Student.objects.all()
    cls = Classes.objects.all()
    pro = Professor.objects.all()
    return render(request, 'data/home.html',{'stud':students, 'cl':cls, 'pr':pro})

def delete_student(request, id):
    del_student = Student.objects.get(id=id)
    del_student.delete()
    return redirect('homepage')

def add_student(request):
    if request.method == 'POST':
        obj = Student()
        obj.name = request.POST['name']
        obj.age = request.POST['age']
        obj.address = request.POST['address']
        obj.Class = Classes.objects.get(class_number = request.POST.get("class"))
        obj.prof = Professor.objects.get(prof_name = request.POST.get("Professor"))
        obj.image = request.FILES.get('im')
        obj.save()
        return redirect('homepage')


def add_professor(request):
    if request.method == 'POST':
        obj = Professor()
        obj.prof_name = request.POST['prof_name']
        obj.save()
        obj.prof_class = Classes.objects.get(class_number = request.POST.get("class"))
        obj.save()
        return redirect('homepage')


def add_Class(request):
    if request.method == 'POST':
        if Classes.objects.filter(class_number = request.POST['class_number55']):
            return HttpResponse('the class already exists')
        else:
            obj = Classes()
            obj.class_number = request.POST['class_number55']  # class_number55 this go to html
            obj.save()
            return redirect('homepage')

    #write this or this
    # cd = request.POST
    # if Classes.objects.filter(class_number = cd['class_number55']):
    #     return HttpResponse('the class already exists')
    # Classes.objects.create(class_number = cd['class_number55'])
    # return redirect('homepage')


def edit_student(request,id):
    if request.method == 'POST':
        obj = Student.objects.get(id=id)
        obj.name = request.POST['name']
        obj.age = request.POST['age']
        obj.address = request.POST['address']
        obj.Class = Classes.objects.get(class_number = request.POST.get("class"))
        obj.prof = Professor.objects.get(prof_name = request.POST.get("Professor"))
        obj.image = request.FILES.get('im')
        obj.save()
        return redirect('homepage')
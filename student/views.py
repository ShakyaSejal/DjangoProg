from django.shortcuts import render
from .models import Student
from django.contrib.auth.decorators import login_required
from .form import StudentForm

# Create your views here.
def student_view(request, id =None):
    student_object =None
    if id is not None:
        student_object = Student.objects.get(id=id)
        print(student_object.name)
    context = {
        "object": student_object,
    }

    return render(request, 'students/student_view.html',context=itcontext)
# def detail_view(request ):
#     print(request.POST)
#     name = request.POST.get('name')
#     course = request.POST.get('course')
#     print(name, course)
#     context = {}
#     return render(request, 'students/details.html',context=context)


@login_required
def detail_view(request, id=None ):
    student_object = None
    context = {}
    form = StudentForm()
    context["form"] = form
    
    if request.method == "POST":
        # print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            student_object = form.save()
            context ["form"] =student_object
            # name = form.cleaned_data.get('name')
            # course = form.cleaned_data.get('course')
            # print(name, course)
            # student_object = Student.objects.create(name = name , course = course)
            # context["object"] = student_object
            # context["created"] = True
        
    return render(request, 'students/details.html',context=context)



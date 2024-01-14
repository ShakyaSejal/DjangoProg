from django import forms
from django.shortcuts import render
from .models import Student

class StudentForm( forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'course',
        ]

    def cleaned(self):
        data =  self.cleaned_data
        print(data)
        name =  data.get("name")
        qs = Student.objects.filter(name_iextract=name)
        if qs.exists():
            self.add_error("name",f"this name {name} has already been used")
            
        cleaned_name=self.cleaned_data.get('name')


# class StudentForm( forms.Form):
#     name = forms.CharField()
#     course = forms.CharField()

def cleaned_name(self):
    cleaned_name = self.cleaned_data.get("name")
    if cleaned_name == "shrijana":
        raise forms.validationError("not a valid name")
    return self.name.capitalize()

def cleaned_alldata(self):
    return self.name.capitalize().self.course.capitalize()




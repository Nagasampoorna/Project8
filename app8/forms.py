from django import forms
from app8.models import CourseModel,StudentModel
import re
class CourseForm(forms.ModelForm):
    Fee = forms.IntegerField(min_value=3000)
    Date = forms.CharField(widget=forms.DateInput(attrs={'type': 'Date'}), label="Date")
    def clean_course_name(self):
        name = self.cleaned_data['Course_Name']
        res = re.findall(r'^[A-Z a-z]*$', name)
        if res:
            return name
        else:
            print(forms.ValidationError)
            raise forms.ValidationError("Invalid Name")
    def clean_faculty_name(self):
        name = self.cleaned_data['Faculty']
        res = re.findall(r'^[A-Z a-z]*$', name)
        if res:
            return name
        else:
            print(forms.ValidationError)
            raise forms.ValidationError("Invalid Name")
    class Meta:
        model = CourseModel
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        fields = ["Name","Contactno","Email","Password"]
        model = StudentModel
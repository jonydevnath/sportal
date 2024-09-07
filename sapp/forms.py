from django import forms
from .models import Enroll, Notice, Routine

class EnrollForm(forms.ModelForm):
    course_name = forms.CharField(label="Course Name ", widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': ''}), required=True)
    days = forms.CharField(label="Days ", widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': ''}), required=True)
    class_time = forms.CharField(label="Class Time ", widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': ''}), required=True)
    room_no = forms.CharField(label="Room No ", widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': ''}), required=True)

    class Meta:
        model = Enroll
        fields = ['course_name', 'days', 'class_time', 'room_no']

class NoticeForm(forms.ModelForm):
    notice = forms.CharField(label="Notice ", widget=forms.Textarea(attrs={'class': 'form-control mt-2', 'placeholder': ''}), required=True)

    class Meta:
        model = Notice
        fields = ['notice']

class RoutineForm(forms.ModelForm):
    exam_date = forms.CharField(label="Exam Date ", widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': ''}), required=True)
    exam_time = forms.CharField(label="Exam Time ", widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': ''}), required=True)
    course_code = forms.CharField(label="Course Code ", widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': ''}), required=True)
    course_name = forms.CharField(label="Course Name ", widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': ''}), required=True)
    course_credit = forms.CharField(label="Course Credit ", widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': ''}), required=True)
    course_type = forms.CharField(label="Course Type ", widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': ''}), required=True)
    room_no = forms.CharField(label="Room No ", widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': ''}), required=True)

    class Meta:
        model = Routine
        fields = ['exam_date','exam_time','course_code','course_name','course_credit','course_type','room_no']
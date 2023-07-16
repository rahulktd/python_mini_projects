from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from core.models import Students, Complaint, Reply


class StudentForm(UserCreationForm):
    class Meta:
        model = Students
        fields = ("email", "name", "mobile", "standard", 'username', 'password1', 'password2',)

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['message']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
class NotificationForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))


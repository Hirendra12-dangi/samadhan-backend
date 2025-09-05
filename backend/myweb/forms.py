from django import forms
from django import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title','description','category','location','photo']
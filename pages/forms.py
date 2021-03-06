from django import forms
from complexModules.models import scoringModel, gradeModel,submissionModel, roundDetails
from .models import youtubeModel

class scoringForm(forms.ModelForm):
    class Meta:
        model = scoringModel
        fields = "__all__"

class gradeForm(forms.ModelForm):
    class Meta:
        model = gradeModel
        fields = "__all__"

class submissionForms(forms.ModelForm):
    class Meta:
        model = submissionModel
        fields = "__all__"
    
class youtubeForms(forms.ModelForm):
    class Meta:
        model = youtubeModel
        fields = "__all__"

class roundDetailsForm(forms.ModelForm):
    class Meta:
        model = roundDetails
        fields = "__all__"
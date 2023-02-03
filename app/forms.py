from django import forms
from app.models import *
class Model_Topic(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class Model_Webpage(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['name']
        #labels={'topic_name':'tn','url':'ur'}
        #widgets={'name':forms.PasswordInput,'url':forms.Textarea}
        #help_texts={'name':'should not be integer','url':'provide proper url'}
class Model_Access(forms.ModelForm):
    class Meta:
        model=Accessrecord
        fields='__all__'
        
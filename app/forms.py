from django import forms
from app.models import Usersignuptable,Userlogintable
from django.forms import PasswordInput

class Usersignup(forms.ModelForm):
    class Meta:
        model=Usersignuptable
        fields="__all__"
        labels={"name":"Name","email":"Email","contact":"Contact No",
                "username":"Username","pas":"Password"}
        widgets = {"pas": PasswordInput}
class Userlogin(forms.ModelForm):
    class Meta:
        model=Userlogintable
        fields="__all__"
        widgets = {"pas": PasswordInput}
        labels={"usrname":"Username","pas":"Password"}
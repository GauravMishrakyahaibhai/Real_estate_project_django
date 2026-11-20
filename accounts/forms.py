from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm



class SignUpForm(UserCreationForm):
    
    username=forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter username'
        }),
        error_messages={
            'required':"Please enter username"
        }
    )
    
    
    email=forms.EmailField(
            widget=forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Enter email'
            }),
            error_messages={
                'required':"Please enter valid email"
            }
        )
    
    password1=forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Enter password'
        }),
        error_messages={
            'required':"Please enter password"
            }
        )
    
    password2=forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Enter confirm password'
        }),
            error_messages={
                'required':"Please enter confirm password"
            }
        )
    
    
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        

class SignInForm(AuthenticationForm):
    
    username=forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter username'
        }),
        error_messages={
            'required':"Please enter username"
        }
    )

    
    password=forms.CharField(
            widget=forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Enter password'
            }),
            error_messages={
                'required':"Please enter password"
            }
        )
    
    
    class Meta:
        model=User
        fields=["username","password"]
from django import forms
from django.forms import ModelForm, DateInput
from .models import UserProfile,Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email address is already in use.")
        else:
            return email
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        # fields = ['birth_date', 'blood_group', 'genre', 'address', 'phone',
        #           'nationality', 'religion', 'marital_status', 'biodata', 'profession', 'image']
        exclude=['user',]


class ContactForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'content']
        widgets = {
            
            'content': forms.Textarea(attrs={'placeholder': 'Say Anything you want to say.'})
        }
        labels = {
            'content':'Your Words',
        }
class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError(
    #             "This email address is already in use.")
    #     else:
    #         return email
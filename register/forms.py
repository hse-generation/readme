from account.models import Users
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, DateInput, DateTimeInput, EmailInput, \
    ImageField, forms


class RegistrationForm(ModelForm):
    class Meta:
        model = Users
        fields = ['login', 'email', 'password']

        widgets = {
            'login': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин',
                'name': 'login'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту',
                'name': 'email',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль',
                'name': 'password'
            }),
        }

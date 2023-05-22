from account.models import Users
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, DateInput, DateTimeInput, EmailInput, \
    ImageField, forms, FileInput, NumberInput


class AccountForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'last_name', 'about', 'email', 'birthdate', 'profile_picture', 'pages_per_day']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
                'name': 'name',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию',
                'name': 'last_name'
            }),
            'pages_per_day': NumberInput(attrs={
                'class': 'form-control',
                'name': 'pages_per_day'
            }),
            'about': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация о вас',
                'name': 'about'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту',
                'name': 'email',
            }),
            'birthdate': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год рождения',
                'name': 'birthdate',
            }),
            'profile_picture': FileInput(attrs={
                'class': 'form-control',
            })
        }

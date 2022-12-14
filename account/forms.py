from account.models import Users
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, DateInput, DateTimeInput, EmailInput, \
    ImageField, forms


class AccountForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'last_name', 'login', 'about', 'email', 'birthdate']

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
            'login': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин',
                'name': 'login'
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
        }

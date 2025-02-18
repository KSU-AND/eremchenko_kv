from django.contrib.auth.forms import UserCreationForm, SetPasswordMixin
from ..models import User


class RegistrationForm(UserCreationForm):
    password1, password2 = SetPasswordMixin.create_password_fields('Пароль*', 'Пароль ещё раз*')
        
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'telegram')
        labels = {'username': 'Никнейм*',
                  'first_name': 'Имя',
                  'last_name': 'Фамилия',
                  'email': 'Почта',
                  'telegram': 'Телеграм',
                  }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field_name in ['username', 'telegram', 'password1', 'password2']:
            self.fields[field_name].help_text = None

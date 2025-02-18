from django.contrib.auth.forms import UserChangeForm
from ..models import User


class ProfileForm(UserChangeForm):
    password = None

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
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None

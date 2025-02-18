from django.contrib.auth.forms import UserCreationForm
from ..models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'telegram', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field_name in ['username', 'telegram', 'password1', 'password2']:
            self.fields[field_name].help_text = None

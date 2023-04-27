from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["screen_name", "email"]
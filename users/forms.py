from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'avatar', 'phone', 'country']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'phone', 'country']

class EmailAuthenticationForm(AuthenticationForm):
    # Переопределяем поле username, чтобы оно принимало Email
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))

    def confirm_login_allowed(self, user):
        # проверка is_active, если регистрация требует подтверждения
        if not user.is_active:
            raise forms.ValidationError("Этот аккаунт неактивен.", code='inactive')



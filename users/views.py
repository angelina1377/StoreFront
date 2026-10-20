from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegisterForm, ProfileForm, EmailAuthenticationForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # ОТПРАВКА ПИСЬМА
            send_mail(
                subject='Добро пожаловать в StoreFront!',
                message=f'Привет, {user.email}! Ваш аккаунт успешно создан.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )
            return redirect('users:profile')
        # Если форма не валидна, она вернется в шаблон с ошибками автоматически
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    # Используем стандартный LoginView, но передаем нашу форму
    return LoginView.as_view(
        template_name='users/login.html',
        authentication_form=EmailAuthenticationForm
    )(request)


@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'users/profile_edit.html', {'form': form})

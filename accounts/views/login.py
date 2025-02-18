from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from ..forms.login import LoginForm


class LoginView(View):
    def __init__(self):
        super().__init__()
        self.context = {'title': 'Вход', 'button': 'Войти'}

    def get(self, request):
        self.context['form'] = LoginForm()
        return render(request, 'accounts.html', self.context)
    
    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('fpt')
        self.context['form'] = form
        return render(request, 'accounts.html', self.context)

from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login

from ..forms.registration import RegistrationForm


class RegistrationView(View):
    def __init__(self):
        super().__init__()
        self.context = {'title': 'Регистрация', 'button': 'Зарегистрироваться'}

    def get(self, request):
        self.context['form'] = RegistrationForm()
        return render(request, 'accounts.html', self.context)
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('fpt')
        self.context['form'] = form
        return render(request, 'accounts.html', self.context)

from django.views import View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from ..forms.profile import ProfileForm


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def __init__(self):
        super().__init__()
        self.context = {'title': 'Личный кабинет', 'button': 'Сохранить'}

    def get(self, request):
        self.context['form'] = ProfileForm(instance=request.user)
        return render(request, 'accounts.html', self.context)
    
    def post(self, request):
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        self.context['form'] = form
        return render(request, 'accounts.html', self.context)
            
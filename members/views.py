from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View

# Create your views here.


class login_user(View):
    template_name = 'login.html'

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('artists/create')
        else:
            messages.success(
                request, 'There was An Error Logging in, Try Again...')
            return redirect('artists/')

    def get(self, request):
        return render(request, self.template_name, {})

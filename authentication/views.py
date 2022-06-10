from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm
from .models import UserToDo


# {% csrf_token %}
#             {% for field in form %}
#                 <p>
#                     <label class="form_label">{{ field.label }}</label><br>
#                     {{ field }}
#                 </p>
#             {% endfor %}
#             <button class="btn" type="submit">Sign up</button>
#             {{ message }}


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'sign_up.html'

    def form_valid(self, form):
        user = UserToDo(username=form.cleaned_data['username'], email=form.cleaned_data['email'],
                        password=make_password(form.cleaned_data['password']))
        user.save()
        user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        login(self.request, user)
        return redirect('/')


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
            else:
                message = 'Incorrect email or password'
                return render(request, 'sign_in.html', {'form': form, 'message': message})
            if not form.cleaned_data['remember_me']:
                request.session.set_expiry(None)
            return redirect('/')
        return render(request, 'sign_in.html', {'form': form, 'message': message})
    else:
        form = LoginUserForm()
    return render(request, 'sign_in.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')

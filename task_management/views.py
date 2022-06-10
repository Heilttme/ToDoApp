from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, FormView

from .forms import TaskToDoForm
from .models import ToDo


class TasksToDo(ListView, FormView):
    form_class = TaskToDoForm
    model = ToDo
    template_name = 'tasks_to_do.html'

    def form_valid(self, form):
        title = form.cleaned_data['title']
        additional_information = form.cleaned_data['additional_information']
        time_expiration = form.cleaned_data['time_expiration']
        user = self.request.user

        todo = ToDo(title=title, additional_information=additional_information, time_expiration=time_expiration,
                    user=user)
        todo.save()
        return redirect('to_do_tasks')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TasksToDo, self).get_context_data(**kwargs)
        context['form'] = TaskToDoForm()
        return context


class CompletedTasks(ListView):
    model = ToDo
    template_name = 'completed_tasks.html'


def delete_task(request, id):
    ToDo.objects.filter(pk=id).delete()
    return redirect('/to_do_tasks')


def finish_task(request, id):
    todo = ToDo.objects.get(pk=id)
    todo.is_finished = True
    todo.save()
    return redirect('/to_do_tasks')
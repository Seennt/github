from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from application.todo_list import models, forms
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.shortcuts import get_list_or_404, redirect
from application.todo_list.pagination import Pages
from django.contrib import messages


# Create your views here.
class List(LoginRequiredMixin, generic.ListView):
    login_url = 'authenticate:login'
    # redirect_field_name = 'todo-list:create'
    template_name = 'todo_list/index.html'
    paginate_by = 10

    # Load the companies
    def get_queryset(self):
        actions = get_list_or_404(models.Action.objects.order_by('completed', 'created'))
        return actions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = ['completed', 'created', 'description', 'subject', 'filed']

        try:
            page = int(self.kwargs['page'])
        except KeyError:
            page = 1

        # Set pagination for companies
        paginator = Pages(self.object_list, self.paginate_by)

        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        # Hook function 'pages_to_show' to object 'pages'.
        setattr(pages, 'pages_to_show', paginator.pages_to_show(page))
        context['pages'] = pages

        return context


class Action(generic.CreateView):
    model = models.Action
    fields = ['description', 'subject']

    def post(self, request, *args, **kwargs):
        if 'cancel' in self.request.POST:
            return redirect('todo-list:index')
        else:
            return super(Action, self).post(request, *args, **kwargs)

    def get_success_url(self):
        if 'add' in self.request.POST:
            messages.add_message(
                self.request,
                messages.INFO,
                'Action: "%s" is listed.' % self.request.POST.get('description')
            )
            return reverse_lazy('todo-list:create')
        elif 'return' in self.request.POST:
            messages.add_message(
                self.request,
                messages.SUCCESS,
                'Action: "%s" is listed.' % self.request.POST.get('description')
            )
            return reverse_lazy('todo-list:index')
        else:
            return reverse_lazy('todo-list:index')


class Detail(SuccessMessageMixin, generic.UpdateView):
    model = models.Action
    form_class = forms.ActionForm
    success_url = reverse_lazy('todo-list:index')
    template_name_suffix = '_update'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = forms.ActionFormSet(self.request.POST, instance=self.object)
            context['formset'].full_clean()
        else:
            context['formset'] = forms.ActionFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():

            if 'completed' in self.request.POST:
                self.object.completed = True

                if self.request.POST['detail_set-0-explanation']:
                    self.object = form.save()
                    formset.instance = self.object
                    formset.save()
                    self.success_message = 'Action is completed!'
                    return super().form_valid(form)
                else:
                    messages.warning(self.request, 'Action can\'t be completed as there is no explanation given.')
                    return redirect(self.success_url)
            else:
                self.object = form.save()
                formset.instance = self.object
                formset.save()
                self.success_message = 'Action is updated, an explanation added/removed or modified.'
                return super().form_valid(form)

        else:
            return self.render_to_response(self.get_context_data(form=form))


class Remove(SuccessMessageMixin, generic.DeleteView):
    model = models.Action
    success_url = reverse_lazy('todo-list:index')
    success_message = 'Action: "%(description)s" is deleted.'
    template_name_suffix = '_delete'

# -*- coding: utf-8 -*-
""" Module: views as part of: todo_list

    Created by: Reinier on 18-10-2017. Django appears to be a MVC framework, but you call the Controller the “view”,
    and the View the “template”. A view is a callable which takes a request and returns a response. This can be more
    than just a function, and Django provides an example of some classes which can be used as views.

    Examples:
        class AboutView(TemplateView):
            template_name = "about.html"

    TODO:
        - Use TODO comments for code that is temporary, a short-term solution, or good-enough but not perfect.

"""
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
        if 'filter' in self.request.GET:
            print('test')
            filter_val = self.request.GET.get('filter', None)
            actions = get_list_or_404(models.Action.objects.filter(subject=filter_val).order_by('completed', 'created'))
        else:
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

        context['unique_action_subject_list'] = models.Action.objects.distinct('subject')

        return context


class Action(generic.CreateView):
    """: The class: "Action", is part of module: "views".

    Add a action to the database.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.

    Args:
        model (object) : A object that represents the Action table.
        fields (list) : List that contains the fields that needs to be added.
    """

    model = models.Action
    fields = ['description', 'subject']

    def post(self, request, *args, **kwargs):
        """18-10-2017: The method: "post", is part of class: "Action".

        Handles POST requests, instantiating a form instance with the passed POST variables and then checked for
        validity. When a action is cancelled a redirect will be done.

        Args:
            request (list): Posted data.

        Returns:
            object: Posted action content.

        """

        if 'cancel' in self.request.POST:
            return redirect('todo-list:index')
        else:
            return super(Action, self).post(request, *args, **kwargs)

    def get_success_url(self):
        """18-10-2017: The method: "get_success_url", is part of class: "Action".

        get_success_url() is just providing somewhere to redirect to, which gets used in the default implementation of
        form_valid().

        Returns:
            str: Redirect to URL.

        """
        if 'add' in self.request.POST:
            messages.add_message(
                self.request,
                messages.INFO,
                'Action: "%s" is Added, please continue.' % self.request.POST.get('description')
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
    """: The class: "Detail", is part of module: "views".

    Add a detailed information(Explanation) to action a certain action, and store this information in table detail.
    Explanation are provided via a formset/jquery.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.

    Args:
        model (object) : A object that represents  the Detail table.
        form_class (object) : A object that holds the detailed form that should be displayed.
        success_url (str) : URL to go to after added a explanation.
        template_name_suffix (str) : The UpdateView page displayed. Eg. action_update.html
    """

    model = models.Action
    form_class = forms.ActionForm
    success_url = reverse_lazy('todo-list:index')
    template_name_suffix = '_update'

    def get_context_data(self, **kwargs):
        """18-10-2017: The method: "get_context_data", is part of class: "Action".

        Representing the template context. The keyword arguments provided will make up the returned context.

        Returns:
            dict: context data for displaying the object.

        """
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = forms.ActionFormSet(self.request.POST, instance=self.object)
            context['formset'].full_clean()
        else:
            context['formset'] = forms.ActionFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        """18-10-2017: The method: "form_valid", is part of class: "Action".

        This method is called when valid form data has been POSTed. It should return an HttpResponse.

        Args:
            form (object): Action form object to validate.

        Returns:
            str: Redirects to the success_url

        """
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
                self.success_message = 'Action is updated, an explanation is added/removed or modified.'
                return super().form_valid(form)

        else:
            return self.render_to_response(self.get_context_data(form=form))


class Remove(SuccessMessageMixin, generic.DeleteView):
    class Remove(object):
        """: The class: "Remove", is part of module: "views".

        Remove a action from the database.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.

        Args:
            model (object) : A record of the table action.
            success_url (str) : URL to go to after successfull removal.
            success_message (str) : A message that is displayed on the delete page conformation.
            template_name_suffix (str) : The DeleteView page displayed. Eg. action_delete.html
        """

    model = models.Action
    success_url = reverse_lazy('todo-list:index')
    success_message = 'Action: "%(description)s" is deleted.'
    template_name_suffix = '_delete'

from django.forms.models import inlineformset_factory, ModelForm
from application.todo_list import models


# Simplify the case of working with related objects via a foreign key.
# Create a formset that allows you to edit roadmaps belonging to a particular scenario.
class ActionForm(ModelForm):
    name = 'Todo action'

    class Meta:
        model = models.Action
        fields = ['description', 'subject']

ActionFormSet = inlineformset_factory(
    models.Action,
    models.Detail,
    fields=['explanation'],
    extra=1,
    can_delete=True,
)

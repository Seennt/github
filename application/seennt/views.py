from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'seennt/index.html')

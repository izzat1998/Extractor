from django.shortcuts import render

# Create your views here.
from django.views import View


class PostView(View):
    def get(self, request):
        return render(request, 'index.html', context={'message': "Hello q1wertgyhy"})

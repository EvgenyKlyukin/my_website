from django.shortcuts import render


def homepage(request):
    template_name = 'base.html'
    return render(request, template_name)

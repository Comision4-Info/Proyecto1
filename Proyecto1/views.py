from django.shortcuts import render

def index(request):
    
    template_name = 'index.html'
    nombres = ['Ceci','Andres','Leo','Jose']
    contexto = {'nombres': nombres}

    return render(request,template_name,contexto)
from django.shortcuts import render
from computerApp.models import Machine

def index(request) :
    machines = Machine.object.all()

    context = {
        'machines': machines ,
    }
    return render(request, 'template/index.html', context)

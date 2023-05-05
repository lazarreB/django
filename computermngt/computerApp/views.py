from django.shortcuts import render
from computerApp.models import Machine, Personne, get_object_or_404

def index(request) :
    machines = Machine.objects.all()

    context = {
        'machines': machines ,
    }
    return render(request, 'index.html', context)


def machine_list_view(request) :
    machines = Machine.objects.all()
    context = {'machines': machines }
    return render(request, 'computerApp/machine_list.html', context)

def personne_list_view(request) :
    personnes = Personne.objects.all()
    context = {'personnes': personnes }
    return render(request, 'computerApp/personne.html', context)

def machine_detail_view(request) :
    machine = get_object_or_404(Machine, id=pk)
    context = {'machine': machine }
    return render(request, 'computerApp/machine_detail.html', context)
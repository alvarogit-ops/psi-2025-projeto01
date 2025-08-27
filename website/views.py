from django.shortcuts import render
from website.models import Contexto, Elenco, Info_Site

def inicio(request):
    contexto_objeto = Contexto.objects.first()
    contexto  = {}
    
    if contexto_objeto:
        contexto = {
            'info_geral': contexto_objeto.info_geral,
          
        }

    return render(request, "website/inicio.html", {'contexto': contexto})

def equipe(request):
    elenco = Elenco.objects.all()       
    contexto = {'elenco': elenco}
    return render(request, "website/equipe.html", contexto)

def sobre(request):
    info_site = Info_Site.objects.first()
    contexto = {}
    if info_site:
        contexto = {
        'descricao:': info_site.descricao,
        'autores': info_site.get_autores_list(),
    }
    return render(request, "website/sobre.html", {'info_site': contexto})

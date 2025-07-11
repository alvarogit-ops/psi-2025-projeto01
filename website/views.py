from django.shortcuts import render

def inicio(request):
    contexto = {
        'info_geral': 'Stranger Things é uma série de suspense e ficção científica da Netflix, criada pelos Irmãos Duffer. Situada nos anos 80, a trama acompanha o desaparecimento de um garoto e o surgimento de uma garota com poderes sobrenaturais.',
        'imagem_url': 'imagens/grupo.jpg',
    }
    return render(request, "website/inicio.html", contexto)

def equipe(request):
    elenco = [
        {'nome': 'Millie Bobby Brown', 'idade': 20, 'posicao': 'Eleven', 'local': 'Marbella, Espanha', 'foto': 'imagens/millie.jpg'},
        {'nome': 'Finn Wolfhard', 'idade': 21, 'posicao': 'Mike Wheeler', 'local': 'Vancouver, Canadá', 'foto': 'imagens/finn.jpg'},
        # ... acrescente os outros 9 membros aqui
    ]
    contexto = {'elenco': elenco}
    return render(request, "website/equipe.html", contexto)

def sobre(request):
    info_site = {
        'descricao': 'Este é um projeto fictício criado para fins educacionais. Desenvolvido por Seu Nome.',
        'autores': ['Seu Nome', 'Outro Autor'],
    }
    return render(request, "website/sobre.html", {'info_site': info_site})

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "website/index.html")

def sobre(request):
    return(render(request, "website/sobre.html"))

def post(request):
    return(render(request, "website/post.html"))

def contato(request):
    return(render(request, "website/post.html"))

"""""
def index(request):
    postagens = [
        {
            "id": 1,
            "titulo": "Minha primeira postagem",
            "subtitulo": "Nessa postagem o conteúdo é muito importante.",
            "autor": "James Wilson",
            "data": "27 de junho de 2025"
        },
        {
            "id": 2,
            "titulo": "Minha segunda postagem",
            "subtitulo": "Outra postagem interessante.",
            "autor": "Ana Souza",
            "data": "28 de junho de 2025"
        }
    ]
    return render(request, "website/index.html", {"postagens": postagens})

"""""


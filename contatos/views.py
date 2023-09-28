from django.shortcuts import render
from .models import Amigo
from .serializers import AmigoSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here.


def index(request):
    if request.GET.get("q"):
        amigos = Amigo.objects.filter(nome__icontains=request.GET["q"])
    else:
        amigos = Amigo.objects.all()

    return render(request, "index.html", {"amigos": amigos})


def detalhar(request, id):
    amigo = amigos = Amigo.objects.get(id=id)
    return render(request, "detalhar.html", {"amigo": amigo})


class AmigoViewSet(ReadOnlyModelViewSet):
    queryset = Amigo.objects.all()
    serializer_class = AmigoSerializer

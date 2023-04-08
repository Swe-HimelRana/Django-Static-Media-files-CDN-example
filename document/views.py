from django.shortcuts import render
from .models import Document
# Create your views here.
def index(request):
    all_docs = Document.objects.all()
    return render(request, 'index.html', {"docs": all_docs})
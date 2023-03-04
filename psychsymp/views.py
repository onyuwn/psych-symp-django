from django.shortcuts import render
from .models import Update

def index(request):
    return render(request, 'psychsymp/index.html')

def news(request):
    latest_updates = Update.objects.order_by("-date")
    context = {'latest_updates': latest_updates}
    return render(request, 'psychsymp/news.html', context)
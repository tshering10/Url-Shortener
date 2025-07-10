from django.shortcuts import render, redirect
from .models import ShortUrl
from .forms import UrlForm
from django.http import HttpResponseRedirect, Http404
# Create your views here.

def home(request):
    short_url = None
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url_instance = form.save()
            short_url = request.build_absolute_uri(f"/{url_instance.short_url}")
    else:
        form = UrlForm()
    return render(request, "link/home.html", {"form":form, "short_url":short_url})

def return_to_orginal(request, short_url):
    try:
        url = ShortUrl.objects.get(short_url=short_url)
        return HttpResponseRedirect(url.original_url)
    except ShortUrl.DoesNotExist:
        raise Http404("Short Url not found!")
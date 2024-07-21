from django.http import HttpResponse
from django.shortcuts import render


def home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {"page_title": my_title}
    html_template = "home.html"
    return render(request, html_template, my_context)


3

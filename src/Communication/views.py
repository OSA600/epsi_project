from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):
    # render (request, "templates")

    return render(request, "index.html", context={"user": "Zoely", "date": datetime.now()})




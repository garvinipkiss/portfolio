from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect

from django.db import transaction
# Create your views here.
def index(request):
    return render(request, 'index.html')

from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db.models import Count
from .models import deliveries, matches
# Create your views here.


def home(request):
    return render(request, 'IPL/base.html')


def problem1(request):
    result = list(matches.objects.values('season').annotate(
        Count('season')).order_by('season'))

    return JsonResponse({'data': result}, json_dumps_params={'indent': 2})


def problem1_graph(request):
    # get the list of dictionary
    result = matches.objects.values('season').annotate(
        Count('season')).order_by('season')

    values = []
    for res in result:
        values.append([res['season'], res['season__count']])

    context = {
        'values': values,
    }
    return render(request, 'IPL/graph1.html', context)

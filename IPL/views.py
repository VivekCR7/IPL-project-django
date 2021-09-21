from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db.models import Count, Sum
from .models import deliveries, matches
# Create your views here.


def home(request):
    return render(request, 'IPL/base.html')


def problem1(request):
    result = list(matches.objects.values('season').annotate(
        Count('season')).order_by('season'))

    return JsonResponse({'data': result}, json_dumps_params={'indent': 2})


def problem1_graph(request):
    return render(request, 'IPL/graph1.html')


def problem2(request):
    result = list(matches.objects.values('winner', 'season').annotate(
        Count('winner')).order_by('season'))

    return JsonResponse({'data': result}, json_dumps_params={'indent': 2})


def problem2_graph(request):
    return render(request, 'IPL/graph2.html')


def problem3(request):
    result = list(deliveries.objects.filter(match_id__season=2016).values(
        'batting_team').annotate(Sum('extra_runs')).order_by('extra_runs__sum'))

    return JsonResponse({'data': result}, json_dumps_params={'indent': 2})


def problem3_graph(request):
    return render(request, 'IPL/graph3.html')


def problem4(request):
    result = list(deliveries.objects.filter(match_id__season=2015).values('bowler').annotate(
        eco=Sum('total_runs') / Count('over', distinct=True)).order_by('eco')[:10])

    return JsonResponse({'data': result}, json_dumps_params={'indent': 2})


def problem4_graph(request):
    return render(request, 'IPL/graph4.html')

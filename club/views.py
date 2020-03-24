from django.shortcuts import render, get_object_or_404

from django.shortcuts import render_to_response

from django.http import HttpResponse

from .models import vd_event

from datetime import datetime, timedelta



def eventslist(request):
    #return HttpResponse("<h1>Список мероприятий клуба активных путешествий INSLED</h1>")
    #return render(request, "index.html", {})
    queryevent = vd_event.objects.all
    content = {"title": "Список мероприятий клуба активных путешествий INSLED", "object_list": queryevent,} 
    return render(request, "index.html", content)

def eventFilter(request, pk):
    queryevent=vd_event.objects.all
    if pk == '1': 
        queryevent=vd_event.objects.all
    elif pk == '2':
        now=datetime.now()
        queryevent=vd_event.objects.filter(data_begin=now)
    elif pk == '3':
        now1=datetime.now()
        now=datetime.now() - timedelta(minutes=60*24*7)
        queryevent=vd_event.objects.filter(data_begin__gte=now,data_begin__lte=now1)
    elif pk == '4':
        now1=datetime.now()
        now=datetime.now() - timedelta(minutes=60*24*30)
        queryevent=vd_event.objects.filter(data_begin__gte=now,data_begin__lte=now1)
    elif pk == '5':
        now1=datetime.now()
        now=datetime.now() - timedelta(minutes=60*24*365)
        queryevent=vd_event.objects.filter(data_begin__gte=now,data_begin__lte=now1)
        
    elif pk == '6':
        now=datetime.now()
        queryevent=vd_event.objects.filter(data_begin__gte=now)
        
    content = {"title": "Список мероприятий клуба активных путешествий INSLED", "object_list": queryevent,} 
    return render(request, "index.html", content)
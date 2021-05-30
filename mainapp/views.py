from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import datetime
@login_required


def index(request):
    today = datetime.date.today()
    context = {
        'page_title': 'дата',
        'today': today,



    }
    return render(request, 'mainapp/index.html', context)


#def clare(request):
#    hour = datetime.time.hour()
#    context = {
#        'page_title': 'дата',
 #       'hour': hour,



#    }
#    return render(request, 'mainapp/index.html', context)
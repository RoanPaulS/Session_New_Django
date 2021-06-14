from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def new_Session_Count(request):
    count = request.session.get('counts',0)
    totalCount = int(count)+1
    request.session['counts'] = totalCount
    exp_date = request.session.get_expiry_date
    details = {'newCount' : totalCount , 'expiry_date' : exp_date}
    return render(request , 'sessionNew.html' , context = details)

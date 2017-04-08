# !python
# log/views.py
import time
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import classroom, labs, requestTable, User
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.shortcuts import redirect
from .forms import EventForm

# Create your views here.
@login_required(login_url='accounts/login/')
def home(request):
    print(request.user.mobile_number)

    vclassroom = classroom.objects.values('block').order_by('block')
    vlabs = labs.objects.values('block').order_by('block')

    seen = set()
    seen1 = set()

    new_class = []
    new_class1 = []

    for d in vclassroom:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_class.append(d)

    for d in vlabs:
        t = tuple(d.items())
        if t not in seen1:
            seen1.add(t)
            new_class1.append(d)

    return render(request, "home.html", {'classroom': new_class, 'labs': new_class1})


@login_required(login_url="accounts/login/")
def classrooms(request, block_name):
    classes = classroom.objects.filter(block=block_name)
    return render(request, "classrooms.html", {"rooms": classes})


@login_required(login_url="accounts/login/")
def lab(request, block_name):
    lab_fetch = labs.objects.filter(block=block_name)
    return render(request, "labs.html", {"rooms": lab_fetch})


@login_required(login_url="accounts/login/")
def roomnumber(request, room_number, block_name):
    form = EventForm(initial={'sender': User.get_username()})
    print()
    return render(request, "calendar.html", {"number": room_number,
                                             "block1": block_name,
                                             "form": form})


@login_required(login_url="accounts/login/")
def labnumber(request, room_number, block_name):
    return render(request, "calendar.html", {"number": room_number,"block_name":block_name})


@login_required(login_url="accounts/login/")
def auditorium(request):
    return render(request, "calendar.html", {"number": "Auditorium"})


@login_required(login_url="accounts/login/")
def eventlist(request):
    if request.is_ajax():
        start = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(request.GET['start']))))
        end = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(request.GET['end']))))
        entries = requestTable.objects.filter(startDateTime__range=(start, end)).all()
        json_list = []
        for entry in entries:
            json_entry = {'start': str(entry.startDateTime), 'end': str(entry.endDateTime), 'allDay': False,
                          'title': entry.description, 'overlap': False,
                          'room_number': entry.room_number}
            json_list.append(json_entry)
        return HttpResponse(json.dumps(json_list, cls=DjangoJSONEncoder), content_type='application/json')


@login_required(login_url="accounts/login/")
def notifications(request):
    user_login = 'faculty'  # student
    # extract id of student

    if user_login == 'faculty':
        username = 'Amit Dhar'
        rows = requestTable.objects.filter(granter=username, booking_status=0).exclude(booking_status=2)
        return render(request, "notifications.html", {'rows': rows, 'type': 'faculty'})
    elif user_login == 'student':
        userid = 'iit2013199'
        rows = requestTable.objects.filter(reserved_by=userid)
        return render(request, "notifications.html", {'rows': rows, 'type': 'student'})


@login_required(login_url="login/")
def nothandler(request, pk, status):
    if request.method == "POST":
        row = requestTable.objects.get(id=pk)
        print(status)
        if status == '1':
            row.booking_status = 1
            row.save()
        else:
            row.booking_status = 2
            row.save()

    return redirect('notifications')


@login_required(login_url="accounts/login/")
def saveEvents(request):
    form = EventForm(request.POST)

    if form.is_valid():
        form.cleaned_data['sender'] = User.username
        form.save()
    else:
        return HttpResponse(form.errors)

    return HttpResponse("Sucess")

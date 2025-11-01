from django.shortcuts import render
from . models import USERS_DATA
from . forms import USERS_INFO

# Create your views here.
# ...existing code...
def create(request):
    if request.method == 'POST':
        frm = USERS_INFO(request.POST)
        if frm.is_valid():
            frm.save()
            frm = USERS_INFO()  # reset form after successful save (or redirect to avoid resubmit)
    else:
        frm = USERS_INFO()
    return render(request, 'index.html', {'frm': frm})


def view(request):
    info=USERS_DATA.objects.all()
    return render(request,"data.html",{"datas":info})
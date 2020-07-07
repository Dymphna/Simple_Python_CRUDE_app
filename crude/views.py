from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CrudeForm
from .models import Crude


# Create your views here.
def crude_list(request):
    crudes = Crude.objects.all()
    context ={ "crude_list": crudes }
    return render(request, "crude/crude_list.html", context)


def crude_detail(request, id):
    crude= Crude.objects.get(id=id)
    context = {"crude": crude}
    return render(request, "crude/crude_detail.html", context)


def crude_create(request):
    form =CrudeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, "crude/crude_create.html", context)

def crude_update(request, id):
    crude= Crude.objects.get(id=id)
    form = CrudeForm(request.POST or None,instance=crude)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, "crude/crude_update.html", context)


def crude_delete(request, id):
    crude = Crude.objects.get(id=id)
    crude.delete()
    return redirect("/")
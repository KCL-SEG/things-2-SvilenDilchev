from django.shortcuts import render
from things.forms import ThingForm


def home(request):

    form = ThingForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'home.html', {'form': form})

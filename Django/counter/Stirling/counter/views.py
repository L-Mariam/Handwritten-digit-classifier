from django.shortcuts import render, get_object_or_404
from .models import Counter

# Create your views here.

def index(request):
    if len(Counter.objects.filter(key='counter')) == 0:
        counter = Counter(keys='counter',value=0)
        counter.save()
    else:
        counter = get_object_or_404(Counter, key='counter')

    counter.value+=1
    counter.save()
    context = {'value':counter.value}
    return render(request, 'counter/index.html', context)

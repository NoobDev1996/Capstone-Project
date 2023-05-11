from django.shortcuts import render
from. models import Tourdate

# Create your views here.
def tourdates(request):
    tourdates = Tourdate.objects.all()
    context = {'tourdates': tourdates}
    return render(request, 'tourdates.html', context)
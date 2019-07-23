from django.shortcuts import render, redirect, HttpResponse
from  . forms import FormMotor
from . models import Motor, Dealer
from django.db.models import Q
# Create your views here.
def search(request):
    try:
        q = request.GET.get('search')
    except:
        q = None
    if q:
        motor = Motor.objects.filter(Q(nama__icontains=q) | Q(thn_produksi__icontains=q) | Q(cc_motor__icontains=q))
        dealer = Dealer.objects.filter(Q(nama__icontains=q) | Q(alamat__icontains=q))
    
        data = {
            'motor' : motor,
            'dealer': dealer
        }
    else:
        data = {}

    return render(request, 'index.html', data)

def index(request):
    list_motor = Motor.objects.all()
    form = FormMotor(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            form = FormMotor()

    context = {
        'list_motor': list_motor,
        'form': form
    }
    return render(request, 'motor/index.html', context)

def edit(request, id):
    motor  = Motor.objects.get(id=id)
    form = FormMotor(request.POST, instance=motor)
    if request.method == 'POST':
        form.save()
    
    context = {
        'motor': motor
    }
    return render(request, 'motor/edit.html', context)


def update(request, id):
    pass

def delete(request, id):
    motor = Motor.objects.get(id=id)
    motor.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))
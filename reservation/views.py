from .models import Reservation
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import ReserveTableForm
from django.contrib.auth.decorators import login_required

def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
            return redirect('reservation:thank_you')

    context = {'form': reserve_form}
    return render(request, 'reservation/reservation.html', context)

def thank_you(request):
    return render(request ,'reservation/thank_you.html')

@login_required
def reservation_management(request):
    """ Display Reservations """
    reservation_management = Reservation.objects.all()
    context = {
        'reservation_management' : reservation_management,
    }

    return render(request, 'reservation/reservation_management.html', context)


@login_required
def delete_reservation(request, reservation_id):
    """ Delete a reservation """
    reservation_management = get_object_or_404(Reservation, pk=reservation_id)
    reservation_management.delete()
    messages.success(request, 'Successfully deleted reservation.')
    context = {
        'reservation_management' : reservation_management,

        'Reservation.id': Reservation.id,

    }
    return redirect(reverse('reservation:reservation_management'))
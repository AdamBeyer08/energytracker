from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from .models import Drink, Consumption
from datetime import date


def home(request):
    return render(request, 'index.html')


def drinks_list(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks.html', {'drinks': drinks})


@login_required(login_url='login')
def stats(request):
    # HISTORIE (všechny záznamy, ne jen dnešek)
    records = Consumption.objects.filter(user=request.user).order_by('-date')

    # dnešní součet
    today_records = Consumption.objects.filter(user=request.user, date=date.today())
    total_caffeine = sum(r.drink.caffeine_mg * r.amount for r in today_records)

    status = "OK" if total_caffeine <= 400 else "EXCEEDED"

    return render(request, 'stats.html', {
        'total': total_caffeine,
        'status': status,
        'records': records
    })


@login_required(login_url='login')
def add_record(request):
    if request.method == "POST":
        drink_id = request.POST.get('drink')
        amount = request.POST.get('amount')

        Consumption.objects.create(
            user=request.user,
            drink_id=drink_id,
            amount=amount
        )
        return redirect('stats')

    drinks = Drink.objects.all()
    return render(request, 'add_record.html', {'drinks': drinks})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
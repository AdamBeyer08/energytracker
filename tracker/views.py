from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Drink, Consumption  # Import tvých modelů
from datetime import date

# 1. Domovská stránka
def home(request):
    return render(request, 'index.html', {'section': 'home'})

# 2. Seznam všech dostupných nápojů
def drinks_list(request):
    drinks = Drink.objects.all()
    return render(request, 'index.html', {'section': 'drinks', 'drinks': drinks})

# 3. Statistiky uživatele (pouze pro přihlášené)
@login_required
def stats(request):
    # Filtrujeme záznamy přihlášeného uživatele pro dnešní den
    today_records = Consumption.objects.filter(user=request.user, date=date.today())
    
    # Výpočet celkového kofeinu (počet kusů * kofein v nápoji)
    total_caffeine = sum(r.drink.caffeine_mg * r.amount for r in today_records)
    
    # Logika limitu (bezpečný limit je 400 mg)
    limit_status = "OK" if total_caffeine <= 400 else "EXCEEDED"
    
    return render(request, 'index.html', {
        'section': 'stats', 
        'total': total_caffeine, 
        'status': limit_status,
        'records': today_records
    })

# 4. Přidání nového záznamu o konzumaci
@login_required
def add_record(request):
    if request.method == "POST":
        drink_id = request.POST.get('drink')
        amount = request.POST.get('amount')
        
        # Vytvoření záznamu v databázi
        Consumption.objects.create(
            user=request.user, 
            drink_id=drink_id, 
            amount=amount
        )
        return redirect('stats')
    
    drinks = Drink.objects.all()
    return render(request, 'index.html', {'section': 'add', 'drinks': drinks})

# 5. Registrace nového uživatele
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Automatické přihlášení po registraci
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'section': 'register', 'form': form})

# 6. Odhlášení
def logout_view(request):
    logout(request)
    return redirect('home')
from django.shortcuts import render, redirect, get_object_or_404
from pzwebapp.models import Language, User, Exchange
from pzwebapp.forms import LanguageForm, UserForm, ExchangeForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Prikaz svih jezika i mogućnost pretrage


def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        languages = Language.objects.filter(name__icontains=search_query)
    else:
        languages = Language.objects.all()

    form = LanguageForm(request.POST or None)

    # Dodavanje novog jezika
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')

    # Dobijanje svih korisnika i razmjena
    users = User.objects.all()
    exchanges = Exchange.objects.all()

    return render(request, 'index.html', {
        'languages': languages, 
        'form': form,
        'users': users,
        'exchanges': exchanges
    })

    
# Uređivanje jezika


def edit_language(request, id):
    language = get_object_or_404(Language, id=id)
    if request.method == 'POST':
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LanguageForm(instance=language)

    return render(request, 'edit_language.html', {'form': form})

# Brisanje jezika


def delete_language(request, id):
    language = get_object_or_404(Language, id=id)
    if request.method == 'POST':
        language.delete()
        return redirect('index')

    return render(request, 'confirm_delete.html', {'language': language})

# Dodavanje korisnika


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})


def add_exchange(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExchangeForm()
    return render(request, 'add_exchange.html', {'form': form})

# Prikaz svih razmjenas


def exchange_list(request):
    exchanges = Exchange.objects.all()
    return render(request, 'exchange_list.html', {'exchanges': exchanges})


@login_required
def home(request):
    return render(request, 'home.html')


def is_admin(user):
    return user.groups.filter(name='Administrator').exists()


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_section.html')


def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        group_name = request.POST['group']  # 'Administrator' ili 'Korisnik'

        user = User.objects.create_user(username=username, password=password)
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
        user.save()
        return redirect('home')

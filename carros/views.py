from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Carro
from .forms import CarroForm, UserRegistrationForm

class CarListView(ListView):
    model = Carro
    template_name = 'carros/carro_list.html'
    context_object_name = 'carros'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Carro.objects.filter(
                Q(nome__icontains=query) | 
                Q(cor__icontains=query) |
                Q(filial__icontains=query)
            )
        return Carro.objects.all()

@login_required
def carro_create(request):
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carro_list')
    else:
        form = CarroForm()
    return render(request, 'carros/carro_form.html', {'form': form})

@login_required
def carro_update(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('carro_list')
    else:
        form = CarroForm(instance=carro)
    return render(request, 'carros/carro_form.html', {'form': form})

@login_required
def carro_delete(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == 'POST':
        carro.delete()
        return redirect('carro_list')
    return render(request, 'carros/carro_confirm_delete.html', {'carro': carro})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('carro_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

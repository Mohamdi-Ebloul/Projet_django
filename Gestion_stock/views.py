from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Stock.models import StockEn, Sorti


from django.contrib.auth import authenticate, login, logout
from Stock.forms import LoginForm


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('Acceil')
                
    context = {'form': forms, }
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def Aceeil(request):
    total_Stock = StockEn.objects.count()
    total_Sorti = Sorti.objects.count()
    
    context = {
        'Stock': total_Stock,
        'Sorti': total_Sorti,
        
                  }
    return render(request,'Aceeil.html',context)
    

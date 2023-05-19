from django.contrib.auth import  logout, authenticate, login 
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import SignUpForm


def main_page(request):
    return render(
        request=request,
        template_name='app/main_page.html'
    )
    
    
# Login function  

# def sign_in(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request=request, user=user)

#                 return redirect('/')
#     else:
#         form = AuthenticationForm()
                
#     return render(
#         request=request,
#         template_name='app/login.html',
#         context={
#             'form': form
#         } 
#     )


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request=request, user=user)
            
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(
                  request=request, 
                  template_name='app/signup.html',
                  context={'form': form} 
                  )
    

# def logout(request):
#     logout(request=request)
#     return redirect('main_page')
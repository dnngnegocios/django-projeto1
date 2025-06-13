from django.shortcuts import render


# Create your views here.
# def home(request):
#     return render(request,'home.html', context={
#       'nome': 'Ricardo',
#       'email':'ricardo@teste.com.br',

#     })


def home(request):
    return render(request,'home/pages/index.html')




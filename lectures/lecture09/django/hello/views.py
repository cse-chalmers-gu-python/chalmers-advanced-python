from django.shortcuts import render

# Create your views here.

def index(request):
    who = request.GET.get('name', 'random person')
    return render(request, 'hello.html', {'who': who})

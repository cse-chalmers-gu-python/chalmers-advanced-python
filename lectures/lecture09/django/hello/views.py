from django.shortcuts import render

def index(request):
    name = request.GET.get('name', 'person')
    return render(request, 'say_hello.html', {'who': name})

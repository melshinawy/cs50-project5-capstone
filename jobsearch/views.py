from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request,'jobsearch/index.html')

def register(request, profile_type):
    if request.method == 'GET':
        return render(request,'jobsearch/register.html', {
            'profile_type': profile_type
        })
def login(request):
    return render(request, 'jobsearch/login.html')
from django.shortcuts import render

# Create your views here.
def dashboard(requests):
    return render(requests,'dashboard/example.html')
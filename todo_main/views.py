from django.shortcuts import render

# This function is for makng home page work
def home(request):
    return render(request, 'home.html')

from django.shortcuts import render

# Create your views here.
def main(request):
    print('=----------------------------------=-=-=--=--------------------------------------------------')
    return render(request, 'myApp/base.html')
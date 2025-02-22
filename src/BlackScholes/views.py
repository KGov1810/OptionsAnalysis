from django.shortcuts import render

def blackscholes(request):
    return render(request, "BlackScholes/index.html")

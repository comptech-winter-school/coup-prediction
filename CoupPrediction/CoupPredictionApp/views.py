from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'CoupPredictionApp/main.html')


def datasets_page(request):
    return render(request, 'CoupPredictionApp/Review.html')

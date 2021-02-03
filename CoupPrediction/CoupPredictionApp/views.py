from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'CoupPredictionApp/main.html')


def about_page(request):
    return HttpResponse('<h4>Мы команда студентов, которая разрабатывает проект по предсказанию госпереворота '
                        'в той или иной стране, в рамках зимней IT-школы</h4>')

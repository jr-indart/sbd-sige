from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def rep_physical_progress(request):
    return render(request, 'rep_physical_progress.html')
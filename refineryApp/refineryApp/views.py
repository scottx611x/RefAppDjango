from django.shortcuts import render


def categorys(request):
    return render(request, 'categorys.html', {})

def workflows(request):
    return render(request, 'workflows.html', {})
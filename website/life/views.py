from django.shortcuts import render

def life_view(request):
    return render(request, 'life/life-page.html', {'title': 'life'})

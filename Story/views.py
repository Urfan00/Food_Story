from django.shortcuts import render


def create_story(request):
    return render(request, 'create_story.html')


def recipes(request):
    return render(request, 'recipes.html')


def single(request):
    return render(request, 'single.html')


def stories(request):
    return render(request, 'stories.html')

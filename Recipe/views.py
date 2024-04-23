from django.shortcuts import render, get_object_or_404
from .models import Category, Recipe, Tags
from django.views.generic import ListView, DetailView



def recipe_list(request):

    recipes = Recipe.objects.all()

    categories = Category.objects.all()


    context = {
        'recipes': recipes,
        'categories' : categories
    }


    return render(request, 'recipes.html', context)



class RecipeView(ListView):
    model = Recipe
    paginate_by = 1
    template_name = 'recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_delete=False, is_active=True).all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'single.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_delete=False, is_active=True).all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


def recipe_detail(request, pk):

    recipe = Recipe.objects.get(pk=pk)
    # recipe = Recipe.objects.filter(pk=pk).first()
    # recipe = get_object_or_404(Recipe, id=pk)

    tags = Tags.objects.all()

    context = {
        'recipe' : recipe,
        'tags' : tags
    }

    return render(request, 'single.html', context)

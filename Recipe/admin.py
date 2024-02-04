from django.contrib import admin
from Recipe.models import Category, Recipe, Tags


admin.site.register([Category, Recipe, Tags])

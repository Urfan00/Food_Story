from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Tags, Recipe




class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'content')



translator.register(Category, CategoryTranslationOptions)
translator.register(Recipe, RecipeTranslationOptions)
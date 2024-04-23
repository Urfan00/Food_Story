from rest_framework import serializers
from Recipe.models import Category, Recipe




class CategoryReadSerializers(serializers.ModelSerializer):

    recipes = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'recipes']

    def get_recipes(self, obj):
        serializer = RecipeCreateSerializers(obj.recipe_category.all(), many=True)
        return serializer.data


class CategoryCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'image']



class RecipeCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        # fields = ['id', 'title', 'image', 'category']
        fields = '__all__'


class RecipeReadSerializers(serializers.ModelSerializer):
    category = CategoryCreateSerializers()

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'image', 'category', 'is_active', 'is_delete']
        # fields = '__all__'


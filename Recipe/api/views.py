from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from Recipe.api.serializers import CategoryCreateSerializers, CategoryReadSerializers, RecipeCreateSerializers, RecipeReadSerializers
from Recipe.models import Category, Recipe
from rest_framework.response import Response
import django_filters.rest_framework
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# class RecipeAPIview(APIView):

#     def get(self, request, *args, **kwargs):

#         recipes = Recipe.objects.all()
#         seriazlier = RecipeReadSerializers(recipes, context = {'request' : request}, many=True)

#         return Response(seriazlier.data)

#     def post(self, request):
#         serializers = RecipeCreateSerializers(data=request.data, context = {'request' : request})
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=201)
#         return Response(serializers.errors, status=400)



# class RecipeReadUpdateDeleteView(APIView):

#     def get(self, request, *args, **kwargs):
#         id = kwargs['pk']
#         recipe = Recipe.objects.get(id=id)
#         serializer = RecipeReadSerializers(recipe)
#         return Response(serializer.data, status=200)

#     def put(self, request, *args, **kwargs):
#         id = kwargs['pk']
#         recipe = Recipe.objects.get(id=id)
#         recipe_data = request.data
#         serializer = RecipeCreateSerializers(data=recipe_data, instance=recipe)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)

#     def patch(self, request, *args, **kwargs):
#         id = kwargs['pk']
#         recipe = Recipe.objects.get(id=id)
#         recipe_data = request.data
#         serializer = RecipeCreateSerializers(data=recipe_data, partial=True, instance=recipe)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)

#     def delete(self, request, *args, **kwargs):
#         id = kwargs['pk']
#         recipe = Recipe.objects.get(id=id)
#         recipe.delete()
#         return Response(status=204)



class GenericAPIViewSerializerMixin:
    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]
    
    # serializer_classes = {
    #     'GET' : RecipeReadSerializers,
    #     'POST' : RecipeCreateSerializers,
    #     'PUT' : RecipeCreateSerializers,
    #     'PATCH' : RecipeCreateSerializers
    # }

    # def get_serializer_class(self):
    #     return self.serializer_classes[self.request.method]
    #     # if self.request.method == 'GET':
    #     #     return self.serializer_classes['GET']
    #     # elif self.request.method == 'PUT':
    #     #     return self.serializer_classes['PUT']
        






    


class RecipeListview(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'is_active', 'is_delete']
    search_fields = ['title']
    serializer_classes = {
        'GET' : RecipeReadSerializers,
        'POST' : RecipeCreateSerializers
    }


class RecipeReadUpdateDeleteView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_classes = {
        'GET' : RecipeReadSerializers,
        'PUT' : RecipeCreateSerializers,
        'PATCH' : RecipeCreateSerializers
    }
    # lookup_field = 'slug'








class CategoryAPIView(APIView):

    def get(self, request, *args, **kwargs):

        categories = Category.objects.all()

        seriazlier = CategoryReadSerializers(categories, context = {'request' : request}, many=True)

        return Response(seriazlier.data)

    def post(self, request):
        serializers = CategoryCreateSerializers(data=request.data, context = {'request' : request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

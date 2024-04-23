from django.contrib import admin
from Recipe.models import Category, Recipe, Tags
from modeltranslation.admin import TranslationAdmin



class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']


admin.site.register(Tags, TagsAdmin)

admin.site.site_header = 'NEW DJANGO ADMIN PANEL'


class CategoryAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'image', 'is_active', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    list_filter = ['is_active']
    search_fields = ['title']
    ordering = ['-id']

    # fields = ['title']

    # exclude = ['image']


admin.site.register(Category, CategoryAdmin)


class RecipeAdmin(TranslationAdmin):
    fieldsets = (
        ('EN', {'fields': ('title_en', 'short_description_en', 'content_en')}),  # English fields
        ('AZ', {'fields': ('title_az', 'short_description_az', 'content_az')}),  # Azerbaijani fields
        ('TR', {'fields': ('title_tr', 'short_description_tr', 'content_tr')}),  # Turkish fields
        ('RU', {'fields': ('title_ru', 'short_description_ru', 'content_ru')}),  # Russian fields
        ('Additional', {'fields': ('image', 'author', 'category', 'tags', 'is_active', 'is_delete')}),  # Non-translated fields
    )

    list_display = ['id', 'title', 'image', 'get_author_fullname', 'get_author_email', 'category', 'is_active', 'is_delete', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    list_filter = ['is_active', 'is_delete']
    search_fields = ['title', 'author__username', 'category__title']
    ordering = ['-title']

    def get_author_fullname(self, obj):
        return obj.author.get_full_name()

    def get_author_email(self, obj):
        return obj.author.email

    get_author_fullname.short_description = 'Author'
    get_author_email.short_description = 'Author EMAIL'



admin.site.register(Recipe, RecipeAdmin)


from django.contrib import admin

from .models import Article, Category

# Register your models here.
admin.site.register(Category)

class ArticleAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['title', 'author', 'category']}),
		('Date Information', {'fields': ['publ_date']}),
		('Images', {'fields': ['hero_image', 'optional_image']}),
		('Description', {'fields': ['body_text']})
	]

admin.site.register(Article, ArticleAdmin)


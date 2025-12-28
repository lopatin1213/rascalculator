from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'text', 'admin_response')
    search_fields = ('user', )  # Возможность искать отзывы по полю "Пользователь"
    ordering = ('-id', )  # По умолчанию сортировка по последнему добавленному отзыву


from .models import Vote



admin.site.register(Vote)
from django.contrib import admin
from .models import AppRasCalck

# Регистрация модели в админке
@admin.register(AppRasCalck)
class AppRasCalckAdmin(admin.ModelAdmin):
    list_display = ['version', 'file','description', 'is_latest']
    search_fields = ['version', 'description']  # Поля для поиска
    list_filter = ['is_latest']  # Возможность фильтрации по полю "is_latest"


from .models import UserPro

class UserProAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_pro', 'pro_expiration_date')
    list_filter = ('is_pro',)


admin.site.register(UserPro, UserProAdmin)

from .models import news



admin.site.register(news)
from .models import AndroidApp
@admin.register(AndroidApp)
class AndroidAppAdmin(admin.ModelAdmin):
    list_display = ['version', 'file','description', 'is_latest']
    search_fields = ['version', 'description']  # Поля для поиска
    list_filter = ['is_latest']  # Возможность фильтрации по полю "is_latest"

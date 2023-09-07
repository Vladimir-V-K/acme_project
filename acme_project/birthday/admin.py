from django.contrib import admin

from .models import Birthday

admin.site.empty_value_display = 'Планета Земля'


class BirthdayInLine(admin.StackedInline):
    model = Birthday
    extra = 0


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday'
    )


admin.site.register(Birthday, BirthdayAdmin)

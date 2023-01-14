from django.contrib import admin
from result_view.models import ResultView
from django.contrib import admin

# Register your models here.


class ResultAdmin(admin.ModelAdmin):
    list_display = ("pk", "product_name", "publisher", "release_date", "contact_info")

admin.site.register(ResultView, ResultAdmin)
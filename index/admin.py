from django.contrib import admin
from index.models import Company, Production_categories, Advert, Advantages, Advertisement

admin.site.register(Production_categories)
admin.site.register(Company)
admin.site.register(Advertisement)

class AdvantagesInLine(admin.StackedInline):
    model = Advantages
    extra = 1

@admin.register(Advert)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [AdvantagesInLine,]
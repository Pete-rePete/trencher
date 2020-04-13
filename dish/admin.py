from django.contrib import admin

from .models import Dish


class DishAdmin(admin.ModelAdmin):
    model = Dish
    ingredient_limit = 4

    list_display = ("name", "abbreviated_ingredients", "has_url")

    def abbreviated_ingredients(self, obj):
        if not obj.ingredients:
            return ""
        limit = self.ingredient_limit
        if len(obj.ingredients) <= limit:
            return ", ".join(obj.ingredients)
        return (
            ", ".join(obj.ingredients[:limit])
            + f"\u2026 ({len(obj.ingredients)-limit} more)"
        )

    abbreviated_ingredients.short_description = "ingredients"

    def has_url(self, obj):
        return bool(obj.recipe_url)

    has_url.boolean = True


admin.site.register(Dish, DishAdmin)

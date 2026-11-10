from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'disponible') # columnas visibles
    list_filter = ('categoria', 'disponible')                  # filtros disponibles
    search_fields = ('nombre', 'categoria')                    # campos de búsqueda
    ordering = ('nombre', '-precio')                            # orden predeterminado
    list_editable = ('precio', 'stock')                        # campos editables en la lista
    fields = ('nombre', 'categoria', 'precio', 'stock', 'disponible') # campos en formulario

admin.site.register(Producto, ProductoAdmin)
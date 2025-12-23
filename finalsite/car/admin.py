from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    # What fields to show in the list view (the main table)
    list_display = (
        'make', 
        'model', 
        'year', 
        'price', 
        'mileage', 
        'color', 
        'is_sold' # Now safe to use since it's in models.py
    )
    
    # Add filters on the right sidebar for quick searching
    list_filter = ('make', 'fuel', 'transmission', 'year', 'is_sold')
    
    # Add search functionality to the list view
    search_fields = ('make', 'model', 'description')
    
    # Fields that are links to the edit page
    list_display_links = ('make', 'model')
    
    # Fields that can be edited directly from the list view
    list_editable = ('price', 'is_sold')
    
    # Grouping fields in the main edit form
    fieldsets = (
        (None, {
            'fields': ('make', 'model', 'year', 'price', 'is_sold')
        }),
        ('Specifications & Appearance', {
            # Note: We use 'bodyType' to match the case in models.py
            'fields': ('mileage', 'fuel', 'transmission', 'color', 'bodyType'), 
            'classes': ('collapse',), # Makes this section collapsible
        }),
        ('Media & Description', {
            'fields': ('image', 'description')
        }),
    )

# Register the model with the custom admin class
admin.site.register(Car, CarAdmin)

# Customize the Admin Site Header
admin.site.site_header = "Bahins Car Sales Admin Directory"
admin.site.site_title = "Bahins Car Sales Admin"
admin.site.index_title = "Welcome to the Car Inventory Management"
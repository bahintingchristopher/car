# from django.db import models

# # Create your models here.
# car/models.py

from django.db import models

class Car(models.Model):
    # Core fields (from your HTML output)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    # Use DecimalField for price to avoid rounding errors common with floats
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    # Detailed specs (from your JSON data)
    mileage = models.IntegerField()
    fuel = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    bodyType = models.CharField(max_length=50)
    
    # Image path (The path starts with /static/...)
    # We use CharField here because we are only storing the path/URL string.
    # ...
    image = models.ImageField(upload_to='cars/') # This is the change
    description = models.TextField()
    # ...
    # Optional but useful status flag
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        # A human-readable representation, useful in the Admin
        return f"{self.year} {self.make} {self.model} (${self.price})"

    class Meta:
        # Sort by year descending (newest first) by default
        ordering = ['-year']
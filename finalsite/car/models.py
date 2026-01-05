from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    mileage = models.IntegerField()
    fuel = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    bodyType = models.CharField(max_length=50)
    
    # Standard ImageField is best here because you are using 
    # django-cloudinary-storage in your settings.
    image = models.ImageField(upload_to='cars/')
    
    description = models.TextField()
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} (${self.price})"

    class Meta:
        ordering = ['-year']
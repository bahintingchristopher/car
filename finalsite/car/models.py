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
    image = models.ImageField(upload_to='cars/')
    description = models.TextField()
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} (${self.price})"

    class Meta:
        ordering = ['-year']

class TestDriveRequest(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    license_number = models.CharField(max_length=100)
    license_expiry = models.DateField()
    experience = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=100)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Test Drive: {self.full_name} - {self.vehicle_model}"
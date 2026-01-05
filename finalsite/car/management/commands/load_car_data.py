# import json
# from django.core.management.base import BaseCommand
# from car.models import Car 
# from decimal import Decimal

# # ----------------------------------------------------------------------------------
# # This dictionary contains all the car data for bulk loading.
# # The 'image' paths have been updated to be relative to MEDIA_ROOT ('media/cars/').
# # ----------------------------------------------------------------------------------
# CAR_DATA_JSON = {
#     "cars": [
#         {
#             "id": 1,
#             "make": "Toyota",
#             "model": "Corolla",
#             "year": 2020,
#             "price": 18500,
#             "mileage": 32000,
#             "fuel": "Gasoline",
#             "transmission": "Automatic",
#             "color": "White",
#             "bodyType": "Sedan",
#             "image": "cars/toyota_corolla.webp",
#             "description": "Reliable sedan with excellent fuel efficiency and low maintenance costs."
#         },
#         {
#             "id": 2,
#             "make": "Honda",
#             "model": "Civic",
#             "year": 2019,
#             "price": 19900,
#             "mileage": 41000,
#             "fuel": "Gasoline",
#             "transmission": "Manual",
#             "color": "Black",
#             "bodyType": "Sedan",
#             "image": "cars/honda_civic.webp",
#             "description": "Sporty and stylish compact car with great handling and durability."
#         },
#         {
#             "id": 3,
#             "make": "Ford",
#             "model": "Mustang",
#             "year": 2021,
#             "price": 38500,
#             "mileage": 12000,
#             "fuel": "Gasoline",
#             "transmission": "Automatic",
#             "color": "Red",
#             "bodyType": "Coupe",
#             "image": "cars/ford_mustang.webp",
#             "description": "Powerful performance car with a bold design and premium features."
#         },
#         {
#             "id": 4,
#             "make": "Tesla",
#             "model": "Model 3",
#             "year": 2022,
#             "price": 42000,
#             "mileage": 8000,
#             "fuel": "Electric",
#             "transmission": "Automatic",
#             "color": "Blue",
#             "bodyType": "Sedan",
#             "image": "cars/tesla_model_3.webp",
#             "description": "Fully electric sedan with advanced technology and exceptional range."
#         },
#         {
#             "id": 5,
#             "make": "BMW",
#             "model": "X5",
#             "year": 2018,
#             "price": 36000,
#             "mileage": 54000,
#             "fuel": "Diesel",
#             "transmission": "Automatic",
#             "color": "Gray",
#             "bodyType": "SUV",
#             "image": "cars/bmw_x5.webp",
#             "description": "Luxury SUV with strong performance and premium interior comfort."
#         },
#         {
#             "id": 6,
#             "make": "Audi",
#             "model": "A4",
#             "year": 2021,
#             "price": 33000,
#             "mileage": 15000,
#             "fuel": "Gasoline",
#             "transmission": "Automatic",
#             "color": "Silver",
#             "bodyType": "Sedan",
#             "image": "cars/audi_a4.webp",
#             "description": "Stylish and comfortable sedan with excellent driving dynamics."
#         },
#         {
#             "id": 7,
#             "make": "Chevrolet",
#             "model": "Camaro",
#             "year": 2020,
#             "price": 37000,
#             "mileage": 22000,
#             "fuel": "Gasoline",
#             "transmission": "Manual",
#             "color": "Yellow",
#             "bodyType": "Coupe",
#             "image": "cars/chevrolet_camaro.webp",
#             "description": "Muscle car with aggressive styling and thrilling performance."
#         },
#         {
#             "id": 8,
#             "make": "Mercedes-Benz",
#             "model": "GLE",
#             "year": 2019,
#             "price": 45000,
#             "mileage": 30000,
#             "fuel": "Diesel",
#             "transmission": "Automatic",
#             "image": "cars/mercebenz_gle.webp", 
#             "color": "Black",
#             "bodyType": "SUV",
#             "description": "Premium SUV with luxurious interior and smooth ride quality."
#         },
#         {
#             "id": 9,
#             "make": "Hyundai",
#             "model": "Elantra",
#             "year": 2020,
#             "price": 17000,
#             "mileage": 29000,
#             "fuel": "Gasoline",
#             "transmission": "Automatic",
#             "color": "White",
#             "bodyType": "Sedan",
#             "image": "cars/hyunday_elantra.webp", 
#             "description": "Efficient and reliable sedan with a comfortable interior and modern tech features."
#         },
#         {
#             "id": 10,
#             "make": "Kia",
#             "model": "Sportage",
#             "year": 2021,
#             "price": 28000,
#             "mileage": 18000,
#             "fuel": "Gasoline",
#             "transmission": "Automatic",
#             "color": "Blue",
#             "bodyType": "SUV",
#             "image": "cars/kia_sportage.webp",
#             "description": "Compact SUV offering great value, spacious cabin, and strong safety ratings."
#         },
#         {
#             "id": 11,
#             "make": "Nissan",
#             "model": "Altima",
#             "year": 2019,
#             "price": 19500,
#             "mileage": 35000,
#             "fuel": "Gasoline",
#             "transmission": "Automatic",
#             "color": "Gray",
#             "bodyType": "Sedan",
#             "image": "cars/nissan_altima.webp",
#             "description": "Smooth-riding sedan with advanced driver assistance and excellent fuel economy."
#         },
#         {
#             "id": 12,
#             "make": "Volkswagen",
#             "model": "Tiguan",
#             "year": 2022,
#             "price": 33000,
#             "mileage": 9000,
#             "fuel": "Gasoline",
#             "transmission": "Automatic",
#             "color": "Red",
#             "bodyType": "SUV",
#             "image": "cars/volkswagen_tiguan.webp",
#             "description": "Stylish SUV with refined driving dynamics and versatile interior space."
#         },
#         {
#             "id": 13,
#             "make": "Subaru",
#             "model": "Outback",
#             "year": 2021,
#             "price": 34000,
#             "mileage": 17000,
#             "fuel": "Gasoline",
#             "transmission": "Automatic",
#             "color": "Green",
#             "bodyType": "Wagon",
#             "image": "cars/subaro_outback.webp", 
#             "description": "Adventure-ready wagon with all-wheel drive and exceptional safety ratings."
#         },
#         {
#             "id": 14,
#             "make": "Mazda",
#             "model": "CX-5",
#             "year": 2020,
#             "price": 29000,
#             "mileage": 23000,
#             "fuel": "Gasoline",
#             "transmission": "Automatic",
#             "color": "Black",
#             "bodyType": "SUV",
#             "image": "cars/mazda_cx5.webp",
#             "description": "Premium-feeling crossover with great handling, efficiency, and upscale design."
#         },
#         {
#             "id": 15,
#             "make": "Jeep",
#             "model": "Wrangler",
#             "year": 2018,
#             "price": 31000,
#             "mileage": 48000,
#             "fuel": "Gasoline",
#             "transmission": "Manual",
#             "color": "Orange",
#             "bodyType": "SUV",
#             "image": "cars/jeep_wrangler.webp",
#             "description": "Iconic off-road SUV built for adventure with rugged styling and strong capability."
#         }
#     ]
# }


# class Command(BaseCommand):
#     # This 'help' text is what shows when you run 'python manage.py help load_car_data'
#     help = 'Loads initial car inventory data from the embedded JSON structure into the database.'

#     # def handle(self, *args, **options):
#     #     # 1. Clear existing data (optional safety measure)
#     #     # We delete all existing cars to ensure a clean import every time this script runs.
#     #     Car.objects.all().delete()

#     def handle(self, *args, **options):
#         # Check if we already have cars. If we do, don't do anything!
#         if Car.objects.exists():
#             self.stdout.write(self.style.WARNING('Database already has data. Skipping seed.'))
#             return
        
#         cars_to_create = []
        
#         # 2. Prepare data for bulk creation
#         for data in CAR_DATA_JSON['cars']:
            
#             # --- IMAGE PATH LOGIC ---
#             # The 'image' path is now clean and ready to be saved as a media file path.
#             full_path = data['image']
            
#             # Since the path is already clean, we just use it directly.
#             relative_media_path = full_path

#             # 2. Create a Car object instance
#             car = Car(
#                 # Mapping the dictionary keys to the model fields
#                 make=data['make'],
#                 model=data['model'],
#                 year=data['year'],
#                 # Convert the number (integer) to Django's required Decimal type for price
#                 price=Decimal(data['price']), 
#                 mileage=data['mileage'],
#                 fuel=data['fuel'],
#                 transmission=data['transmission'],
#                 color=data['color'],
#                 bodyType=data['bodyType'],
#                 image=relative_media_path, # <-- NOW USING THE CLEAN, MEDIA-READY PATH
#                 description=data['description']
#             )
#             cars_to_create.append(car)
            

#         # 3. Save all objects to the database efficiently 
#         # This executes a single SQL query to insert all 15 records at once.
#         # Car.objects.bulk_create(cars_to_create)

#         # Save to database
#         Car.objects.bulk_create(cars_to_create)
#         self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(cars_to_create)} cars.'))

#         self.stdout.write(
#             self.style.SUCCESS(f'Successfully loaded {len(cars_to_create)} cars into the database.')
#         )

# THIS IS THE NEW CODE WITH CLOUD STORAGE INTEGRATION
import os
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
from car.models import Car

CAR_DATA_JSON = {
    "cars": [
        {
            "id": 1,
            "make": "Toyota",
            "model": "Corolla",
            "year": 2020,
            "price": 18500,
            "mileage": 32000,
            "fuel": "Gasoline",
            "transmission": "Automatic",
            "color": "White",
            "bodyType": "Sedan",
            "image": "toyota_corolla.webp", # Just the filename is enough
            "description": "Reliable sedan with excellent fuel efficiency."
        },
        {
            "id": 2,
            "make": "Honda",
            "model": "Civic",
            "year": 2019,
            "price": 19900,
            "mileage": 41000,
            "fuel": "Gasoline",
            "transmission": "Manual",
            "color": "Black",
            "bodyType": "Sedan",
            "image": "honda_civic.webp",
            "description": "Sporty and stylish compact car with great handling and durability."
        },
        {
            "id": 3,
            "make": "Ford",
            "model": "Mustang",
            "year": 2021,
            "price": 38500,
            "mileage": 12000,
            "fuel": "Gasoline",
            "transmission": "Automatic",
            "color": "Red",
            "bodyType": "Coupe",
            "image": "ford_mustang.webp",
            "description": "Powerful performance car with a bold design and premium features."
        },
        {
            "id": 4,
            "make": "Tesla",
            "model": "Model 3",
            "year": 2022,
            "price": 42000,
            "mileage": 8000,
            "fuel": "Electric",
            "transmission": "Automatic",
            "color": "Blue",
            "bodyType": "Sedan",
            "image": "tesla_model_3.webp",
            "description": "Fully electric sedan with advanced technology and exceptional range."
        },
        {
            "id": 5,
            "make": "BMW",
            "model": "X5",
            "year": 2018,
            "price": 36000,
            "mileage": 54000,
            "fuel": "Diesel",
            "transmission": "Automatic",
            "color": "Gray",
            "bodyType": "SUV",
            "image": "bmw_x5.webp",
            "description": "Luxury SUV with strong performance and premium interior comfort."
        },
        {
            "id": 6,
            "make": "Audi",
            "model": "A4",
            "year": 2021,
            "price": 33000,
            "mileage": 15000,
            "fuel": "Gasoline",
            "transmission": "Automatic",
            "color": "Silver",
            "bodyType": "Sedan",
            "image": "audi_a4.webp",
            "description": "Stylish and comfortable sedan with excellent driving dynamics."
        },
        {
            "id": 7,
            "make": "Chevrolet",
            "model": "Camaro",
            "year": 2020,
            "price": 37000,
            "mileage": 22000,
            "fuel": "Gasoline",
            "transmission": "Manual",
            "color": "Yellow",
            "bodyType": "Coupe",
            "image": "chevrolet_camaro.webp",
            "description": "Muscle car with aggressive styling and thrilling performance."
        },
        {
            "id": 8,
            "make": "Mercedes-Benz",
            "model": "GLE",
            "year": 2019,
            "price": 45000,
            "mileage": 30000,
            "fuel": "Diesel",
            "transmission": "Automatic",
            "image": "mercebenz_gle.webp", 
            "color": "Black",
            "bodyType": "SUV",
            "description": "Premium SUV with luxurious interior and smooth ride quality."
        },
        {
            "id": 9,
            "make": "Hyundai",
            "model": "Elantra",
            "year": 2020,
            "price": 17000,
            "mileage": 29000,
            "fuel": "Gasoline",
            "transmission": "Automatic",
            "color": "White",
            "bodyType": "Sedan",
            "image": "hyunday_elantra.webp", 
            "description": "Efficient and reliable sedan with a comfortable interior and modern tech features."
        },
        {
            "id": 10,
            "make": "Kia",
            "model": "Sportage",
            "year": 2021,
            "price": 28000,
            "mileage": 18000,
            "fuel": "Gasoline",
            "transmission": "Automatic",
            "color": "Blue",
            "bodyType": "SUV",
            "image": "kia_sportage.webp",
            "description": "Compact SUV offering great value, spacious cabin, and strong safety ratings."
        },
        {
            "id": 11,
            "make": "Nissan",
            "model": "Altima",
            "year": 2019,
            "price": 19500,
            "mileage": 35000,
            "fuel": "Gasoline",
            "transmission": "Automatic",
            "color": "Gray",
            "bodyType": "Sedan",
            "image": "nissan_altima.webp",
            "description": "Smooth-riding sedan with advanced driver assistance and excellent fuel economy."
        },
        {
            "id": 12,
            "make": "Volkswagen",
            "model": "Tiguan",
            "year": 2022,
            "price": 33000,
            "mileage": 9000,
            "fuel": "Gasoline",
            "transmission": "Automatic",
            "color": "Red",
            "bodyType": "SUV",
            "image": "volkswagen_tiguan.webp",
            "description": "Stylish SUV with refined driving dynamics and versatile interior space."
        },
        {
            "id": 13,
            "make": "Subaru",
            "model": "Outback",
            "year": 2021,
            "price": 34000,
            "mileage": 17000,
            "fuel": "Gasoline",
            "transmission": "Automatic",
            "color": "Green",
            "bodyType": "Wagon",
            "image": "subaro_outback.webp", 
            "description": "Adventure-ready wagon with all-wheel drive and exceptional safety ratings."
        },
        {
            "id": 14,
            "make": "Mazda",
            "model": "CX-5",
            "year": 2020,
            "price": 29000,
            "mileage": 23000,
            "fuel": "Gasoline",
            "transmission": "Automatic",
            "color": "Black",
            "bodyType": "SUV",
            "image": "mazda_cx5.webp",
            "description": "Premium-feeling crossover with great handling, efficiency, and upscale design."
        },
        {
            "id": 15,
            "make": "Jeep",
            "model": "Wrangler",
            "year": 2018,
            "price": 31000,
            "mileage": 48000,
            "fuel": "Gasoline",
            "transmission": "Manual",
            "color": "Orange",
            "bodyType": "SUV",
            "image": "Jeep_wrangler.webp",
            "description": "Iconic off-road SUV built for adventure with rugged styling and strong capability."
        }
    ]
}
class Command(BaseCommand):
    help = 'Uploads images from GitHub static folder to Cloudinary and seeds the database'

    def handle(self, *args, **options):
        # 1. Clear existing data to avoid duplicates or broken links
        self.stdout.write(self.style.WARNING('Clearing old data...'))
        Car.objects.all().delete()
        
        for data in CAR_DATA_JSON['cars']:
            # 2. Construct the local path to the image
            filename = os.path.basename(data['image'])
            # Ensure this path matches your folder structure exactly
            image_local_path = os.path.join(
                settings.BASE_DIR, 'car', 'static', 'car', 'images', filename
            )

            # 3. Instantiate the Car object (not saved to DB yet)
            car = Car(
                make=data['make'],
                model=data['model'],
                year=data['year'],
                price=Decimal(str(data['price'])), 
                mileage=data['mileage'],
                fuel=data['fuel'],
                transmission=data['transmission'],
                color=data['color'],
                bodyType=data['bodyType'],
                description=data['description']
            )

            # 4. Handle the Image Upload
            if os.path.exists(image_local_path):
                with open(image_local_path, 'rb') as f:
                    # Wrapping the standard Python file in Django's File wrapper
                    django_file = File(f, name=filename)
                    
                    # .save(save=True) uploads to Cloudinary AND saves the Car record
                    car.image.save(filename, django_file, save=True)
                
                self.stdout.write(self.style.SUCCESS(f'✅ Uploaded & Saved: {data["make"]} {data["model"]}'))
            else:
                # Save without an image if the file isn't found
                car.save()
                self.stdout.write(self.style.ERROR(f'❌ Image NOT found: {image_local_path}'))

        self.stdout.write(self.style.SUCCESS('🚀 Process complete. All cars processed!'))
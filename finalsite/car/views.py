# from django.shortcuts import render, redirect

# def home(request):
#     return render(request, 'car/index.html')

# def inventory(request):
#     return render(request, 'car/inventory.html')

# def contact(request):
#     return render(request, 'car/contact.html')

# def thankyou(request):
#     if request.method == "GET":
#         context = {
#             "fullName": request.GET.get("fullName"),
#             "phone": request.GET.get("phone"),
#             "email": request.GET.get("email"),
#             "licenseNumber": request.GET.get("licenseNumber"),
#             "licenseExpiry": request.GET.get("licenseExpiry"),
#             "experience": request.GET.get("experience"),
#             "vehicleModel": request.GET.get("vehicleModel"),
#             "testDriveDate": request.GET.get("testDriveDate"),
#             "testDriveTime": request.GET.get("testDriveTime"),
#             "notes": request.GET.get("notes"),
#         }
#         return render(request, "car/thankyou.html", context)

#     return redirect("contact")

  # car/views.py

from django.shortcuts import render, redirect
# 1. Import your Car Model
from .models import Car 
# from .models import Car # Assuming Car is in the same app's models.py

def home(request):
    # fetch 3 random car objects from the database
    hot_picks = Car.objects.order_by('?') [:3]
    context = {
            'hot_picks':hot_picks,
    }

    return render(request, 'car/index.html', context)

def inventory(request):
    # 2. Retrieve data using the Django ORM
    # Get all Car objects from the database, ordered by year (newest first)
    all_cars = Car.objects.all().order_by('-year') 
    
    # 3. Create the context dictionary
    context = {
        'cars': all_cars, # Pass the list of cars to the template using the key 'cars'
    }
    
    # 4. Render the template, passing the context
    return render(request, 'car/inventory.html', context)

def contact(request):
    return render(request, 'car/contact.html')

# (The rest of your functions, like thankyou, remain the same)
def thankyou(request):
    if request.method == "GET":
        context = {
            "fullName": request.GET.get("fullName"),
            "phone": request.GET.get("phone"),
            "email": request.GET.get("email"),
            "licenseNumber": request.GET.get("licenseNumber"),
            "licenseExpiry": request.GET.get("licenseExpiry"),
            "experience": request.GET.get("experience"),
            "vehicleModel": request.GET.get("vehicleModel"),
            "testDriveDate": request.GET.get("testDriveDate"),
            "testDriveTime": request.GET.get("testDriveTime"),
            "notes": request.GET.get("notes"),
        }
        return render(request, "car/thankyou.html", context)

    return redirect("contact")
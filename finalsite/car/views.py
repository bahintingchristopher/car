from django.shortcuts import render, redirect
from .models import Car, TestDriveRequest 

def home(request):
    # If the database is empty, this won't crash, but make sure 
    # your index.html handles empty lists.
    hot_picks = Car.objects.order_by('?')[:3]
    context = {'hot_picks': hot_picks}
    return render(request, 'car/index.html', context)

def inventory(request):
    all_cars = Car.objects.all().order_by('-year') 
    context = {'cars': all_cars}
    return render(request, 'car/inventory.html', context)

def contact(request):
    return render(request, 'car/contact.html')

def thankyou(request):
    if request.method == "POST":
        full_name = request.POST.get("fullName")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        license_num = request.POST.get("licenseNumber")
        license_exp = request.POST.get("licenseExpiry")
        exp = request.POST.get("experience")
        model_req = request.POST.get("vehicleModel")
        drive_date = request.POST.get("testDriveDate")
        drive_time = request.POST.get("testDriveTime")
        notes = request.POST.get("notes")

        # Save to Database
        TestDriveRequest.objects.create(
            full_name=full_name, 
            phone=phone, 
            email=email,
            license_number=license_num, 
            license_expiry=license_exp,
            experience=exp, 
            vehicle_model=model_req,
            preferred_date=drive_date, 
            preferred_time=drive_time,
            notes=notes
        )

        context = {
            "fullName": full_name,
            "phone": phone,
            "email": email,
            "licenseNumber": license_num,
            "licenseExpiry": license_exp,
            "experience": exp,
            "vehicleModel": model_req,
            "testDriveDate": drive_date,
            "testDriveTime": drive_time,
            "notes": notes,
        }
        return render(request, "car/thankyou.html", context)

    return redirect("contact")
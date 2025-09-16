from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from core.form import CustomUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "index.html")
def about_us(request):
    return render(request, "Pages/about.html")

def donarLogin(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=name, password=password)  # now uses email backend
        print("Authenticated user:", user)

        if user is not None:
            login(request, user)
            return redirect("Donar_Dash")
        else:
            print("Invalid username or password")

    return render(request, "Pages/organDonation.html")
def donarSignup(request):
    if request.method == "POST":
        print("Form data received:", request.POST)
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save() 
            name=request.POST.get("username")
            father=request.POST.get("father_name")
            email=request.POST.get("email")
            phone=request.POST.get("mobile")
            city=request.POST.get("city")
            dob=request.POST.get("dob")
            photo=request.FILES['profile_img']
            gender=request.POST.get("gender")
            donar_details = Donor_Details(
                user_id=user,
                name=name,
                father=father,
                email=email,
                phone=phone,
                city=city,
                dob=dob,
                photo=photo,
                gender=gender,
            )
            donar_details.save()
            print("User created:", user.id)
            return redirect("Donar_login_info")
        else:
            print("Invalid form:", form.errors)
    else:
        form = CustomUserForm()

    return render(request, "Pages/organDonation_signup.html", {"form": form})

def donarDashboard(request):
    return render(request,"Donar/Donar_dashboard.html")
def pledge(request):
    return render(request, "Pages/Pledge.html")
@login_required
def donor_myprofile(request):
    try:
        data = Donor_Details.objects.get(user_id=request.user)
    except Donor_Details.DoesNotExist:
        messages.error(request, "Profile not found!")
        return redirect("Donar_Dash")
    if request.method == "POST":
        data.name = request.POST.get("name")
        data.father = request.POST.get("father")
        data.phone = request.POST.get("mobile")
        data.city = request.POST.get("city")
        data.dob = request.POST.get("dob")
        data.gender = request.POST.get("gender")
        if request.FILES.get("photo"):
            data.photo = request.FILES["photo"]

        data.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("Donor_myprofile")  # Reload page

    return render(request, "Donar/donor_myprofile.html", {"data": data})

@login_required
def upload_test_results(request):
    if request.method == "POST":
        donor = request.user
        data = request.POST
        file = request.FILES.get("reports")

        def parse_float(value):
            return float(value) if value else None

        def parse_int(value):
            return int(value) if value else None

        donor_testdetails=DonorTestResult.objects.create(
            donor=donor,
            visual_acuity=data.get("visual_acuity") or None,
            corneal_thickness=parse_float(data.get("corneal_thickness")),
            iop=parse_float(data.get("iop")),

            creatinine=parse_float(data.get("creatinine")),
            bun=parse_float(data.get("bun")),
            gfr=parse_float(data.get("gfr")),

            alt=parse_float(data.get("alt")),
            ast=parse_float(data.get("ast")),
            bilirubin=parse_float(data.get("bilirubin")),
            albumin=parse_float(data.get("albumin")),

            blood_group=data.get("blood_group") or None,
            hla_typing=data.get("hla_typing") or None,
            hemoglobin=parse_float(data.get("hemoglobin")),
            wbc=parse_int(data.get("wbc")),
            platelets=parse_int(data.get("platelets")),

            bp=data.get("bp") or None,
            ecg=data.get("ecg") or None,
            glucose=parse_float(data.get("glucose")),
            hiv=data.get("hiv") or None,
            hbv=data.get("hbv") or None,
            hcv=data.get("hcv") or None,
            vdrl=data.get("vdrl") or None,

            reports=file,
        )
        return redirect("Donar_Dash")

    return render(request, "Donar/UploadTestResults.html")

def logout_view(request):
    logout(request)
    return redirect("index")
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Donor_Details(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    father = models.CharField(max_length=50)
    email  = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='Donar_images/', null=True)
    gender = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Donor_registration"

from django.db import models
from django.contrib.auth.models import User

class DonorTestResult(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="test_results")
    
    # Eye
    visual_acuity = models.CharField(max_length=20, blank=True, null=True)
    corneal_thickness = models.FloatField(blank=True, null=True)
    iop = models.FloatField(blank=True, null=True)

    # Kidney
    creatinine = models.FloatField(blank=True, null=True)
    bun = models.FloatField(blank=True, null=True)
    gfr = models.FloatField(blank=True, null=True)

    # Liver
    alt = models.FloatField(blank=True, null=True)
    ast = models.FloatField(blank=True, null=True)
    bilirubin = models.FloatField(blank=True, null=True)
    albumin = models.FloatField(blank=True, null=True)

    # Tissue
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    hla_typing = models.CharField(max_length=100, blank=True, null=True)
    hemoglobin = models.FloatField(blank=True, null=True)
    wbc = models.IntegerField(blank=True, null=True)
    platelets = models.IntegerField(blank=True, null=True)
    bp = models.CharField(max_length=15, blank=True, null=True)
    ecg = models.CharField(max_length=50, blank=True, null=True)
    glucose = models.FloatField(blank=True, null=True)
    hiv = models.CharField(max_length=10, blank=True, null=True)
    hbv = models.CharField(max_length=10, blank=True, null=True)
    hcv = models.CharField(max_length=10, blank=True, null=True)
    vdrl = models.CharField(max_length=10, blank=True, null=True)
    reports = models.FileField(upload_to="test_reports/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Test Results for {self.donor.username} - {self.created_at.date()}"


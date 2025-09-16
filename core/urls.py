from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="index"),
    path("about_us", about_us, name="about_us"),  
    path("donarLogin", donarLogin, name="Donar_login_info"),
    path("donar_register",donarSignup,name="Donar_register_details"),
    path("donar/dashboard",donarDashboard,name="Donar_Dash"),
    path("pledge", pledge, name="pledge"),
    path("Donor_myprofile",donor_myprofile,name="Donor_myprofile"),
    path("donar/upload-test-results/", upload_test_results, name="upload_test_results"),
    path("logout",logout_view,name="log_out"),
]

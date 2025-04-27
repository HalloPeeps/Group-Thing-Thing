from django.urls import path
from products import views

urlpatterns = [
        path("", views.landing_page, name="landing"), # "default" page (displays when there's no / in the URL)
        # about us page
        # our project page
]
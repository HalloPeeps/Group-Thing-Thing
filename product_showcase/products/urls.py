from django.urls import path
from products import views
urlpatterns = [
        path("", views.landing_page, name="landing-page"), # "default" page (shows when there's no / in the URL)
        path("products", views.product_home, name="product-home"),
        path("products/apple", views.product_detail, name="product-detail"), # still needs to be changed so that it's dynamic (i.e.: /products/honeycrisp-apple)
        path("about-us", views.about_us, name="about-us"),
        path("our-project", views.our_project, name="our-project"),
        path("dummy-page", views.dummy_page, name="dummy-page")
]

from django.urls import path
from products import views
urlpatterns = [
        path("", views.landing_page, name="landing-page"), # "default" page (shows when there's no / in the URL)
        path("products", views.product_home, name="product-home"),
        path("products/<str:apple>/", views.product_detail, name="product-detail"),
        path("about-us", views.about_us, name="about-us"),
        path("our-project", views.our_project, name="our-project"),
        path("view-cart", views.view_cart, name="view-cart"),
        path("feedback-form", views.log_message, name="feedback-form"),
        path("dummy-page", views.dummy_page, name="dummy-page") # ignore; was just used for testing
]

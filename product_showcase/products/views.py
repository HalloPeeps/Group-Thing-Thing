from django.shortcuts import render

# Create your views here.

# viewing product (still needs to be made): make a list of different apples, take specific apple from list depending on what product the user clicks on, pass that apple through a view function

def landing_page(request):
    return render(request, "products/landing.html")

def product_home(request):
    return render(request, "products/product_home.html")
    print("FOR TESTING PURPOSES: You're in the products page! Apples should be displayed here.")

def product_detail(request):
    return render(request, "products/view_product.html")
    print("FOR TESTING PURPOSES: You should see this page after clicking on an apple!")

def about_us(request):
    print("FOR TESTING PURPOSES: Displays information about our development team!")
    return render(request, "products/about_us.html")

def our_project(request):
    return render(request, "products/our_project.html")
    print("FOR TESTING PURPOSES: Displays our project timeline!")

def dummy_page(request):
    print("FOR TESTING PURPOSES: Displays dummy page!")
    return render(request, "products/dummy_page.html")

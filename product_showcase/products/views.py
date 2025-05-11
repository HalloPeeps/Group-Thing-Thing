from django.shortcuts import render
from django.http import Http404
from datetime import datetime
from django.shortcuts import redirect
from products.forms import LogMessageForm
from products.models import LogMessage
from django.views.generic import ListView
from .forms import CommentForm
from .models import Comment

apples = { # to be inserted into view function for product details
    "Cortland Apple" : "products/images/CortlandApple.png",
    "Empire Apple" : "products/images/EmpireApple.png",
    "Fuji Apple" : "products/images/FujiApple.png",
    "Gala Apple" : "products/images/GalaApple.png",
    "Golden Delicious" : "products/images/GoldenDelicious.png",
    "Granny Smith" : "products/images/GrannySmith.png",
    "Honeycrisp Apple" : "products/images/Honeycrisp.png",
    "Red Delicious" : "products/images/RedDelicious.png",
}
# Create your views here.

# viewing product (still needs to be made): make a list of different apples, take specific apple from list depending on what product the user clicks on, pass that apple through a view function

def landing_page(request):
    return render(request, "products/landing.html")

def product_home(request):
    return render(request, "products/product_home.html")
    print("FOR TESTING PURPOSES: You're in the products page! Apples should be displayed here.")


def product_detail(request, apple):
    if apple not in apples: # if the apple does not exist, raise a 404 error
        raise Http404("Apple not found.")
    apple_img_link = apples[apple] # sets apple_img to the link of the apple image in "apples" dictionary

    comments = Comment.objects.filter(product_slug=apple).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product_slug = apple
            comment.save()
            return redirect('product-detail', apple=apple)
    else:
        form = CommentForm()

    return render(request, "products/view_product.html", {
            "apple_image": apple_img_link,
            "apple_name": apple,
            "form": form,
            "comments": comments,
        })

def about_us(request):
    print("FOR TESTING PURPOSES: Displays information about our development team!")
    return render(request, "products/about_us.html")

def our_project(request):
    return render(request, "products/our_project.html")
    print("FOR TESTING PURPOSES: Displays our project timeline!")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("product_home") # this is currently acting weird.
    else:
        return render(request, "products/log_message.html", {"form": form})

def view_cart(request):
    return render(request, "products/cart.html")

def dummy_page(request):
    print("FOR TESTING PURPOSES: Displays dummy page!")
    return render(request, "products/dummy_page.html")

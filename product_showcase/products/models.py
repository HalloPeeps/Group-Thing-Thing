from django.db import models
from django.utils import timezone

# Create your models here.

class LogMessage(models.Model): # for feedback form
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class Comment(models.Model):
    product_slug = models.SlugField()  # This will store the apple name (like 'Fuji', 'Honeycrisp', etc.)
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.product_slug}"
    
class Apple(models.Model):
    variety = models.CharField(max_length=20)
    price = models.IntegerField()
    rating = models.IntegerField()
from django.db import models
from django.utils import timezone
from django.db.models import Sum
from datetime import timedelta

class Customer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @staticmethod
    def get_top_customers():
        six_months_ago = timezone.now() - timedelta(days=180)
        top_customers = (
            Order.objects.filter(order_date__gte=six_months_ago)
            .values('customer')
            .annotate(total_spent=Sum('total_amount'))
            .order_by('-total_spent')[:5]
        )
        return top_customers
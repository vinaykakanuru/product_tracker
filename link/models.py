from django.db import models
from product_tracker.utils import get_link_data

# Create your models here.


class Link(models.Model):
    name = models.CharField(max_length=250, blank=True)
    url = models.URLField()
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('price_difference', '-created_at')

    def save(self, *args, **kwargs):
        product_name, price = get_link_data(self.url)
        curr_price = self.current_price

        if self.current_price:
            if price != curr_price:
                diff = price - curr_price
                self.price_difference = round(diff, 2)
                self.old_price = curr_price
        else:
            self.old_price = 0
            self.price_difference = 0

        self.name = product_name
        self.current_price = price

        super().save(*args, **kwargs)

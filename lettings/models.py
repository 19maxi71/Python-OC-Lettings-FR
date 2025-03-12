from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Address(models.Model):
    """
    Represents a physical address.
    """
    number = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    zip_code = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Represents a property available for letting.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from django.db import models


class FizzBuzz(models.Model):
    # FizzBuzz model stores values of fizz buzz keys and values in the database.
    # Created and Updated fields are added as a standard procedure to track
    # object cretation.
    # It is assumed that the game will from 1, and only positive integers will be used.
    fizz_name = models.CharField(max_length=50, default="Fizz")
    buzz_name = models.CharField(max_length=50, default="Buzz")
    fizz_count = models.PositiveIntegerField(default=3)
    buzz_count = models.PositiveIntegerField(default=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fizz_name}({self.fizz_count}) - {self.buzz_name}({self.buzz_count}) "

    class Meta:
        verbose_name_plural = "Fizz Buzz"

from django.db import models
import string
import random

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

class ShortUrl(models.Model):
    original_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = generate_short_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Short url for: {self.original_url} is {self.short_url}"

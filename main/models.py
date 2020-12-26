from django.db import models
from django.db.models import Model

# Create your models here.


class Story(Model):
    STORY_CHOICES = [
        ("P", "Problems"),
        ("C", "Consequences"),
        ("O", "Opportunities"),
        ("CG", "Career Goals")
    ]

    story_type = models.CharField(
        max_length=2,
        choices=STORY_CHOICES,
    )
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=500)
    content = models.TextField()
    date_added = models.DateTimeField()

    def __str__(self):
        return self.title

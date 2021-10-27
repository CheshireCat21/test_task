from django.db import models


class Message(models.Model):
    author = models.CharField(blank=False, max_length=99)
    email = models.EmailField(blank=False)
    text = models.CharField(blank=False, max_length=99)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

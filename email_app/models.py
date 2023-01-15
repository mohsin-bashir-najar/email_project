from django.db import models
from account.models import Account

# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(
        Account, on_delete=models.SET_NULL, blank=True, null=True)
    recipient = models.ForeignKey(
        Account, on_delete=models.SET_NULL, blank=True, null=True, related_name="messages")
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject}"

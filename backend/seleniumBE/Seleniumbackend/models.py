from django.db import models

class Keyword(models.Model):
    keyword = models.CharField(max_length=255)
    vpn_country = models.CharField(max_length=100)
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.keyword

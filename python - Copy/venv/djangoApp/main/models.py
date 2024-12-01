from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Photo Title")
    image = models.ImageField(upload_to='photos/', verbose_name="Photo File")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

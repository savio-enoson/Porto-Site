from django.db import models


class Project (models.Model):
    title = models.CharField(max_length=64)
    thumbnail = models.ImageField(upload_to="dynamic_photo_path")
    featured = models.BooleanField(default=False)
    brief = models.CharField(max_length=240)
    template_name = models.CharField(max_length=16)
    date = models.DateField()
    topics = models.CharField(max_length=64)
    type = models.CharField(max_length=64, null=True, blank=True)
    instance = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"

    def dynamic_photo_path(instance, filename):
        return f"Static/images/{instance.title}/{filename}"

    thumbnail.upload_to = dynamic_photo_path
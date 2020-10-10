from django.db import models
from django.db.models.deletion import CASCADE
from datetime import timedelta, datetime as dt

# Create your models here.
class Face(models.Model):
    name = models.CharField(max_length=45, blank=False)
    owner = models.ForeignKey(
        "auth.User", related_name="faces_to_remove", on_delete=CASCADE
    )
    img_dir = models.CharField(max_length=180, blank=False)


class Video(models.Model):
    name = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey("auth.User", related_name="videos", on_delete=CASCADE)
    video_dir = models.CharField(max_length=180, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(default=(dt.now() + timedelta(days=1)))
from django.db import models
from django.utils.text import slugify
from django.db.models import Model


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    created_at = (models.DateTimeField(auto_now_add=True),)
    updated_at = (models.DateTimeField(auto_now=True),)

    class Meta:
        # define table name
        db_table = "grete_blog_blog"

    def save(self, *args, **kwargs):
        # Membuat slug dari judul jika belum ada
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

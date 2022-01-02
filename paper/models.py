from django.db import models

# Create your models here.
class post(models.Model):
    STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2, "Delete")
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(primary_key=True, max_length=200, unique=True)
    author = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post", kwargs={"slug": str(self.slug)})
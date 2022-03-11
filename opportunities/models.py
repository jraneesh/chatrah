from django.db import models

class opportunities(models.Model):
    type = [
    (1,"Job Placement"),
    (2,"Internship"),
    (3, "NSS/Social Work"),
    (4,"Other")
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    time = models.DateTimeField()
    content = models.TextField(max_length=500)
    type = models.IntegerField(choices=type, default=4)
    link = models.CharField(max_length=300)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.title
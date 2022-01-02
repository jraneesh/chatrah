from django.db import models

class notification(models.Model):
    years = [
    (1,"I"),
    (2,"II"),
    (3, "III"),
    (4, "IV"),
    (5, "ALL"),
    ]
    sections = [
        (1, "A"),
        (2, "B"),
        (3, "C"),
        (4, "ALL"),
    ]
    depts = [
        (1, "CSE"),
        (2, "CIVIL"),
        (3, "EEE"),
        (4, "IT"),
        (5, "ECE"),
        (6, "MECH"),
        (7, "EIE"),
        (8, "ALL"),
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    time = models.DateTimeField()
    content = models.TextField(max_length=750)
    year = models.IntegerField(choices=years, default=5)
    dept = models.IntegerField(choices=depts, default=8)
    section = models.IntegerField(choices=sections, default=4)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.title
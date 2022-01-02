from django.db import models

class student(models.Model):
    years = [
    (1,"I"),
    (2,"II"),
    (3, "III"),
    (4, "IV"),
    ]
    sections = [
        (1, "A"),
        (2, "B"),
        (3, "C"),
    ]
    depts = [
        (1, "CSE"),
        (2, "CIVIL"),
        (3, "EEE"),
        (4, "IT"),
        (5, "ECE"),
        (6, "MECH"),
        (7, "EIE"),
    ]
    name = models.CharField(max_length=200, default="STUDENT")
    number = models.CharField(max_length=15, unique=True, primary_key=True, default="000000000")
    YoA = models.PositiveIntegerField(default="0000")
    year = models.IntegerField(choices=years, default=1)
    dept = models.IntegerField(choices=depts, default=1)
    section = models.IntegerField(choices=sections, default=1)
    verified = models.BooleanField(default=False, editable=True)

    class Meta:
        ordering = ['-number']

    #def __class__(self):
    #    return self
    


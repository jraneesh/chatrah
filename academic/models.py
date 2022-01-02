from django.db import models

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

class timetable(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="TimeTable")
    year = models.IntegerField(choices=years, default=1)
    dept = models.IntegerField(choices=depts, default=1)
    section = models.IntegerField(choices=sections, default=1)
    timetable = models.ImageField(upload_to='timetable/')

    def __str__(self):
        return self.title
    

class syllabus_credit(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    reg = models.CharField(max_length=4, default="R18")
    dept = models.IntegerField(choices=depts, default=1)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class notebook(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    year = models.IntegerField(choices=years, default=1)
    dept = models.IntegerField(choices=depts, default=1)
    section = models.IntegerField(choices=sections, default=1)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title
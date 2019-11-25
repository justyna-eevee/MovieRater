from django.db import models

class ExtraInfo(models.Model):
    RODZAJE = {
        (0, 'Nieznany'),
        (1, 'Komedia'),
        (2, 'S - F'),
        (3, 'Horror'),
        (4, 'Doramat')
    }
    time = models.IntegerField(default=0)
    rodzaj = models.IntegerField(default=0, choices=RODZAJE)

class Movie(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default="")
    year = models.IntegerField(null=True, blank=True)
    released = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(null=True, blank=True, decimal_places=7, max_digits=10)
    photo = models.ImageField(null=True, blank=True)
    info = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE) #, primary_key=True)

    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.name) + "(" + str(self.year) + ")"


class Review(models.Model):
    text = models.CharField(default="", blank=True, max_length=120)
    starts = models.IntegerField(default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)



class Aktor(models.Model):
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    filmy = models.ManyToManyField(Movie)
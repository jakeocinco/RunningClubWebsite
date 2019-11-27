from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #auto_now_add when post was created
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Meet(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    show = models.BooleanField()
    signuplink = models.CharField(max_length=250)
    activeLink = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    #link = models.CharField(max_length=100)
    #auto_now_add when post was created
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question


class Executives(models.Model):

    PRESIDENT = 'President'
    VICE_PRESIDENT = 'Vice President'
    TREASURER = 'Treasurer'
    SECRETARY = 'Secretary'
    WEB_SOCIAL_MEDIA = 'Web/Social Media'
    ADVISOR = 'Advisor'



    POSITION = (
        (PRESIDENT, 'President'),
        (VICE_PRESIDENT, 'Vice President'),
        (TREASURER, 'Treasurer'),
        (SECRETARY, 'Secretary'),
        (WEB_SOCIAL_MEDIA, 'Web/Social Media'),
        (ADVISOR, 'Advisor'),
    )

    ROTATION = (
        ('0', '0'),
        ('90', '90'),
        ('180', '180'),
        ('270', '270'),
    )

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=16, choices=POSITION, default=PRESIDENT)
    about =  models.TextField()
    email = models.CharField(max_length=100)
    order = models.PositiveIntegerField()
    picture = CloudinaryField('image', blank=True)
    imageRotation = models.CharField(max_length=3, choices=ROTATION, default='0')

    #link = models.CharField(max_length=100)
    #auto_now_add when post was created

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=100)
    longDistance = models.CharField(max_length=100)
    shortDistance = models.CharField(blank=True,max_length=100)
    picture = CloudinaryField('image')
    directionsText = models.TextField(max_length=10000)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.name

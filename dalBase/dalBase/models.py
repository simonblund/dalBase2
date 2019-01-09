from django.db import models
from django.contrib.auth.models import User


class Responder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=100, blank=True)


class Incident(models.Model):
    KOMMUNER = (
        ('035', 'brändö'),
        ('043', 'eckerö'),
        ('060', 'finström'),
        ('062', 'föglö'),
        ('065', 'geta'),
        ('076', 'hammarland'),
        ('170', 'jomala'),
        ('318', 'kökar'),
        ('417', 'lemland'),
        ('478', 'mariehamn'),
        ('736', 'saltvik'),
        ('766', 'sottunga'),
        ('771', 'sund'),
        ('941', 'vårdö'),
        ('295', 'kumlinge'),
        ('438', 'lumparland'),
    )
    message = models.CharField(max_length=400, blank=True)
    start_datetime = models.DateTimeField(auto_created=True, blank=True)
    end_datetime = models.DateTimeField(auto_now=False, blank=True)
    comment = models.CharField(max_length=600, blank=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, blank=True, choices=KOMMUNER)

    def __str__(self):
        return self.start_datetime + "-"+self.address


class Vehicle(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class IncidentUser(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_created=True)
    time_left = models.IntegerField(default=0)
    comment = models.CharField(max_length=150, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.incident+"-"+self.user


class IncidentVehicle(models.Model):
    STATUS = (
        ('1', 'Kvitterad'),
        ('2', 'Framme'),
        ('3', 'Frigjord'),
        ('4', 'På station'),
        ('5', 'På service'),
        ('6', 'Olycka'),
    )
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    km = models.IntegerField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True)
    status = models.CharField(max_length=100, blank=True, choices=STATUS)

    def __str__(self):
        return self.incident+"-"+self.vehicle


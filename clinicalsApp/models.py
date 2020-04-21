from django.db import models

# Create your models here.
class Patient(models.Model):
    lastName = models.CharField(max_length = 20)
    firstName = models.CharField(max_length = 20)
    age = models.IntegerField()

class ClinicalData(models.Model): #many to one relationship (clincaldata to Patient)
    COMPONENT_NAMES = [('hw','Height/Weight'),('bp','Blood Pressure'),('heartrate','Heart Rate')]
    componentName = models.CharField(choices = COMPONENT_NAMES, max_length = 20) # this is a dropdown on the UI
    componentValue = models.CharField(max_length = 20)
    measuredDateTime = models.DateTimeField(auto_now_add = True) #configure intialization to current ddtetime
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)

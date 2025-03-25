from django.db import models

class Doctors(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    job_type = models.CharField(max_length=50)
    doctor_img = models.ImageField(upload_to='static/media')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

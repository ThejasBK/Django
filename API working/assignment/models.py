from django.db import models

# Create your models here.
class UserInformation(models.Model):
    user_id = models.CharField(max_length = 10, primary_key = True) 
    real_name = models.CharField(max_length = 264)
    tz = models.CharField(max_length = 264)

    def __str__(self):
        return self.real_name

class ActivityPeriods(models.Model):
    user_id = models.ForeignKey(UserInformation, on_delete = models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
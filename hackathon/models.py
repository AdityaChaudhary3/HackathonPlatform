from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hackathon(models.Model):
    SUBMISSION_TYPE_CHOICES = [
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    ]
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000,blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    submission_type = models.CharField(max_length=5, choices=SUBMISSION_TYPE_CHOICES, default='link')
    created_at = models.DateTimeField(auto_now_add=True)
    reward = models.CharField(max_length=100)
    created_by = models.ForeignKey(User,related_name='hackathons', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class HackathonParticipant(models.Model):
    hackathon = models.ForeignKey(Hackathon, related_name='participants', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='participating_hackathons', on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    

# class Submission(models.Model):
#     hackathon = models.ForeignKey(Hackathon, related_name='submissions', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, related_name='submissions', on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     summary = models.CharField(max_length=1000)
#     submission = models.TextField()
#     submitted_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.user.username


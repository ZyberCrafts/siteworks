from django.db import models
from django.contrib.auth.models import User 
import datetime

class Profile(models.Model):
    ROLE_CHOICES = [
        ('Employer', 'Employer'),
        ('Worker', 'Worker'),
        ('Ambassador', 'Ambassador'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') 
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)  
    bio = models.TextField(max_length=500, blank=True) 
    phone_number = models.CharField(max_length=15, blank = False, null = False) 
    skills = models.CharField(max_length=30, blank=True)  
    location = models.CharField(max_length=15, blank=True)  
    rating = models.IntegerField(default=1)  
    profile_picture = models.ImageField(upload_to='uploads/profile/')
    def __str__(self):
        return f"{self.user.username} - {self.role}'s profile"
    
class Job(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=300, default='',blank = True, null=True)
    location = models.CharField(max_length= 15)
    budget = models.DecimalField(default = 0, decimal_places= 2, max_digits=6)
    posted_date = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
        
    def __str__(self):
        return f'{self.title}'

        
class Bid(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(default = 0, decimal_places= 2, max_digits=6)
    message = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.job.title} {self.bid_amount}'
    
class Contract(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    agreed_amount = models.DecimalField(default = 0, decimal_places= 2, max_digits=6)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.job.title} {self.worker.username} {self.start_date} {self.end_date} {self.agreed_amount} {self.status}'
    
class Reviews (models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    reviewers = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=10)
    comments = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.contract.job.title} {self.reviewers} {self.rating} {self.comments} {self.created_at}'
    
class Payment(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    amount_paid = models.CharField(max_length=15)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=100)
    status = models.BooleanField(default = False)
    
    def __str__(self):
        return f'{self.contract} {self.amount_paid} {self.status}'
    
class Location(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Associate location with a user
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address

class JobLocation(models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE)  # Associate location with a job
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:20]}"

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"
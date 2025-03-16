from django.db import models

class ContactSubmission(models.Model):
    SERVICE_CHOICES = [
        ('tech_tune_up', 'Tech Tune-Up'),
        ('short_term', 'One-off Short-Term Help'),
        ('long_term', 'Long Term Project Help'),
        ('other', 'Something Else'),
    ]
    
    USED_BEFORE_CHOICES = [
        ('yes', 'I Have'),
        ('no', 'I Have Not'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    used_before = models.CharField(max_length=10, choices=USED_BEFORE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Submission'
        verbose_name_plural = 'Contact Submissions'
    
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

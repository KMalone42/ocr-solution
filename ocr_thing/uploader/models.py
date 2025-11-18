# uploader/models.py
from django.db import models

class UploadedFile(models.Model):
    title = models.CharField(max_length=50, blank=True)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.file.name} - {self.uploaded_at}"

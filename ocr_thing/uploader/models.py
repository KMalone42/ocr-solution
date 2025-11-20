# uploader/models.py
from django.db import models
import uuid

class UploadedFile(models.Model):
    title = models.CharField(max_length=50, blank=True)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    batch_id = models.CharField(max_length=36, default='', blank=True)
    processing_complete = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.file.name} - {self.uploaded_at}"

# uploader/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import FileFieldForm
from .models import UploadedFile

# File upload with batch support
class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = "upload.html"
    success_url = "/success/url/"

    def form_valid(self, form):
        files = form.cleaned_data["file_field"]

        # Primary key for a batch
        batch_id = str(uuid.uuid())

        for f in files:
            # Save each file to database
            UploadedFile.objects.create(
                file=f,
                title=f.name  # Use filename as title, or leave blank
                batch_id=batch_id,
                processing_complete=False # Mark true after successful processing
            )
        return super().form_valid(form)

def upload_success(request):
    batch_id = request.session.get('batch_id')
    return render(request, 'success.html', {'batch_id': batch_id})

# Listener that runs while user is in the processing session
def check_processing_status(request, batch_id):
    """API endpoint to check if processing is complete"""
    files = UploadedFile.objects.filter(batch_id=batch_id)
    
    if not files.exists():
        return JsonResponse({'status': 'error', 'message': 'Batch not found'})
    
    all_complete = all(f.processing_complete for f in files)
    
    return JsonResponse({
        'status': 'complete' if all_complete else 'processing',
        'total': files.count(),
        'completed': files.filter(processing_complete=True).count()
    })

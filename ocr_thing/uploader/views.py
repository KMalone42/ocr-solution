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
        for f in files:
            # Save each file to database
            UploadedFile.objects.create(
                file=f,
                title=f.name  # Use filename as title, or leave blank
            )
        return super().form_valid(form)

def upload_success(request):
    return render(request, 'success.html')


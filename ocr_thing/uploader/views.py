# uploader/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadFileForm, FileFieldForm  # import your actual forms


def handle_uploaded_file(f):
    with open("some/file/name.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})


from django.views.generic.edit import FormView


class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = "upload.html"  # Replace with your template.
    success_url = "/success/url/"  # or reverse(...)

    def form_valid(self, form):
        files = form.cleaned_data["file_field"]
        for f in files:
            # Do something with each file.
            handle_uploaded_file(f)
        return super().form_valid(form)


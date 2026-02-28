from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os

# -------------------------------------------------------
# FILE UPLOAD VIEW
# -------------------------------------------------------

def file_upload(request):

    if request.method == "POST" and request.FILES.get("file_upload"):

        pdf_file = request.FILES["file_upload"]

        # Validate file type
        if not pdf_file.name.endswith(".pdf"):
            return render(request, "fileupload.html", {
                "error": "Only PDF files are allowed!"
            })

        # Save file
        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)
        file_path = fs.path(filename)

        print("File saved at:", file_path)

        # 🔥 Later you will send this file_path to resume analyzer logic

        return render(request, "dashboard.html", {
            "file_name": filename
        })

    return render(request, "fileupload.html")
from django.shortcuts import render
from django.http import HttpResponse
import os

def home(request):
    return render(request, "file_app/home.html")

def vulnerable_page(request):
    return render(request, "file_app/read_file_vulnerable.html")

def safe_page(request):
    return render(request, "file_app/read_file_safe.html")

def read_file_vulnerable(request):
    filename = request.GET.get("file")

    if not filename:
        return HttpResponse("No file specified.")

    try:
        with open(f"uploads/{filename}", "r", encoding="utf-8") as f:
            content = f.read()
        return HttpResponse(content, content_type="text/plain; charset=utf-8")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
    
def read_file_safe(request):
    filename = request.GET.get("file")

    if not filename:
        return HttpResponse("No file specified.")

    base_dir = os.path.abspath("uploads")
    file_path = os.path.abspath(os.path.join(base_dir, filename))

    # Проверка дали файлът остава в uploads
    if not file_path.startswith(base_dir):
        return HttpResponse("Access denied")

    if not os.path.exists(file_path):
        return HttpResponse("File not found")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return HttpResponse(content, content_type="text/plain; charset=utf-8")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
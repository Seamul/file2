from django.shortcuts import render
import glob, os, os.path
from django.conf import settings
from django.http import HttpResponse, Http404, StreamingHttpResponse, FileResponse
# Create your views here.
def file_download(request):
    # do something...
    quickbook_path = os.path.join(settings.MEDIA_ROOT,'documents/',"Accounting_Summary_Automation.docx")
    print("---------------------------")
    print(quickbook_path)
    with open(quickbook_path) as f:
        c = f.read()
    return HttpResponse(c)
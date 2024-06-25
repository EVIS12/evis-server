import requests
from django.http import HttpResponse

from evis.conference.models import ContractFile


class ContractFileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "filetype" in request.GET:
            filetype = request.GET.get("filetype")
            file = ContractFile.objects.filter(type=filetype).first()
            if file:
                file_url = request.build_absolute_uri(file.file.url)
                response = requests.get(file_url)
                if response.status_code == 200:
                    response = HttpResponse(response.content)
                    response["Content-Disposition"] = f"attachment; filename={file.file.name}"
                    return response

        return self.get_response(request)

from django.http import HttpResponse, HttpResponseBadRequest

from .utils import is_optimal


def index(request):
    return HttpResponse(
        "[!] Connected to Boeing 787!<br>[?] Enter how many days this Boeing has been operational (1 to 248): http://localhost:8080/isoptimal?days=[1-248]: "
    )


def isoptimal(request):
    try:
        days = int(request.GET["days"])
        if days <= 0:
            raise ValueError
        res = is_optimal(days)
    except ValueError:
        return HttpResponseBadRequest()
    if res:
        return HttpResponse("[i] Reboot is required")
    else:
        return HttpResponse(f"[i] System is optimal<br>Reboot is required in {248 - days} days")

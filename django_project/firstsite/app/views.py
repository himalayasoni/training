from django.shortcuts import HttpResponse
from django.views import View

from app.services import service
from django.contrib.auth.models import User
import json


def index(request):
    return HttpResponse("home page")


def about(request):
    return HttpResponse("this is about page")


class PlayerView(View):
    def get(self, request):
        return HttpResponse(json.dumps(service.get_data()), content_type="application/json")

    def post(self, request):
        return HttpResponse(json.dumps(service.post_data(json.loads(request.body))), content_type="application/json")


class PlayerParamView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        return HttpResponse(json.dumps(service.get_param_data(pk)), content_type="application/json")

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        return HttpResponse(json.dumps(service.put_param_data(json.loads(request.body), pk)), content_type="application/json")

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        return HttpResponse(json.dumps(service.delete_param_data(pk)), content_type="application/json")
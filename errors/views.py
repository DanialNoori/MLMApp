from django.shortcuts import render
from django.http import JsonResponse
from django.template import RequestContext
# Create your views here.

def page_not_found_view(request):
	status = {'status_code' : '404' , 'description' : 'Page Not Found'}
	response = JsonResponse(status)
	response.status_code = 404
	return response

def server_error_view(request):
	status = {'status_code' : '500' , 'description' : 'Server Error'}
	response = JsonResponse(status)
	response.status_code = 500
	return response

def permission_denied_view(request):
	status = {'status_code' : '403' , 'description' : 'Permission Denied'}
	response = JsonResponse(status)
	response.status_code = 403
	return response

def bad_request_view(request):
	status = {'status_code' : '400' , 'description' : 'Bad Request'}
	response = JsonResponse(status)
	response.status_code = 400
	return response
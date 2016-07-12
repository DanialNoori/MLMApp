from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import AppUser,Address,ParentHood
import random
import string
from django.db import IntegrityError
from .sms import generate_random_token, SendSMS
from django.core.mail import EmailMessage
# Create your views here.


def test(request):
	if request.method == 'GET':
		return render(request, 'home.html')


def login(request):
	if request.method == 'POST':
		if username in request.COOKIES:
			username = request.COOKIES['username']
			user = authenticate(username=username, password=username)
			if user:
				login(request, user)
				status = {'status_code' : '200'}
				return JsonResponse(status)
			else:
				status = {'status' : 'False'} 
		else:
			username = request.POST['username']
			user = authenticate(username=username, password=username)
			if user:
				login(request, user)
				status = {'status_code' : '200'}
				response = JsonResponse(status)
				response.set_cookie('username', username)
				return response
			else:
				status = {'status' : 'False'}
				return JsonResponse(status)


def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		userExists = User.objects.filter(username=username)
		if userExists:
			validationCode = generate_random_token()
			appUserExists = AppUser.objects.get(user=userExists)
			appUserExists.validationCode = validationCode
			appUserExists.save()
			conn = SendSMS(username, validationCode)
			connection_status = conn.text
			status = {'status_code' : '200' , 'conn' : connection_status }
			response = JsonResponse(status)
			return response
		else:
			user = User.objects.create_user(username= username, password=username)
			validationCode = generate_random_token()
			AppUser.objects.create(user=user, validationCode=validationCode)
			conn = SendSMS(username, validationCode)
			connection_status = conn.text
			status = {'status_code' : '200' , 'conn' : connection_status }
			response = JsonResponse(status)
			return response


def validate_registration(request):
	if request.method == 'POST':
		validationCode = request.POST.get('validationCode')
		username = request.POST['username']
		user = User.objects.get(username=username)
		appUser = AppUser.objects.get(user=user)
		if appUser.validationCode == validationCode:
			appUser.validated = True
			appUser.save()
			isValidated = appUser.validated
			status = {'status_code' : '200' , 'isValidated': isValidated}
			response = JsonResponse(status)
			response.set_cookie('username' , username)
			return response
		else:
			wrong_token = 'Wrong Token'
			return JsonResponse({'error' : wrong_token, 'username': username , 'validationCode':validationCode})


def generate_random_mail_token():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))


def sendMail(email, username):
	mailToken = generate_random_mail_token()
	user = User.objects.get(username=username)
	appUser = AppUser.objects.get(user=user)
	appUser.mailToken = mailToken
	appUser.save()
	message = 'Click on the link below to validate your email address:\n'
	message += 'http://192.168.2.111:8000/api/accounts/mail-validation/?mailToken=' + mailToken
	mail = EmailMessage('Verification Code', message,to=[email])
	mail.send()


def validateEmail(request):
	if request.method == 'GET':
		if request.GET.get('mailToken'):
			mailToken = request.GET.get('mailToken')
			appUser = AppUser.objects.get(mailToken=mailToken)
			appUser.emailValidated = True
			appUser.save()
			response = 'Your email has been validated!'
			return response
		else:
			response = 'Token is invalid!'
			return response


def mailIsValid(request):
	if request.method == 'GET':
		if request.GET.get('username'):
			username = request.GET.get('username')	
			user = User.objects.filter(username=username)
			appUser = AppUser.objects.filter(user=user)
			mailIsValid = appUser.emailValidated
			data = {'mailIsValid' : mailIsValid}
			return JsonResponse(data)


def fullRegistration(request):
	if request.method == 'POST':
		picture = request.FILES.get('profilePicture')
		username = request.POST['username']
		user = User.objects.get(username=username)
		appUser = AppUser.objects.get(user=user)
		appUser.profilePicture = picture
		appUser.name = request.POST['name']
		appUser.familyName = request.POST['familyName']
		appUser.fatherName = request.POST['fatherName']
		appUser.birthID = request.POST['birthID']
		appUser.birthDay = request.POST['birthDay']
		appUser.birthMonth = request.POST['birthMonth']
		appUser.birthYear = request.POST['birthYear']
		appUser.gender = request.POST['gender']
		appUser.nationalID = request.POST['nationalID']
		appUser.save()
		state = request.POST['state']
		city = request.POST['city']
		phoneNumber = request.POST['phoneNumber']
		mobileNumber = request.POST['mobileNumber']
		address = request.POST['address']
		postalCode = request.POST['postalCode']
		userAddress = Address.objects.create(state=state, phoneNumber=phoneNumber, city=city, mobileNumber=mobileNumber,
			address=address, postalCode=postalCode)
		email = request.POST['email']
		sendMail(email, username)
		user.email = email
		user.save()
		status = {'status_code': '200'}
		response = JsonResponse(status)
		return response


def parentObject(request):
	if request.method == 'POST':
		parentUsername = request.POST['parentUsername']
		parentUser = User.objects.filter(username=parentUsername)
		parent = AppUser.objects.filter(user=parentUser)
		childUsername = request.POST['childUsername']
		childUser = User.objects.filter(username=childUsername)
		child = AppUser.objects.filter(user=childUser)
		ParentHood.objects.create(parent=parent, child=child)
		status = {'status_code': '200' , 'status' : 'Pending Validation from parent'}
		response = JsonResponse(status)
		return response


def logout(request):
	if request.method == 'POST':
		username = request.POST['username']
		user = User.objects.get(username=username)
		logout(user)
		status = {'status_code' : '200'}
		response = JsonResponse(status)
		return response

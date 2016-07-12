from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import AppUser,Address,ParentHood
import random
import string
from django.db import IntegrityError
from users.sms import generate_random_token, SendSMS
from django.core.mail import EmailMessage
from tasks.models import Task, Scheduler
# Create your views here.


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
			status = {'status_code' : '200', 'conn' : connection_status }
			user = authenticate(username=username, password=username)
			if user:
				login(request, user)
				response = HttpResponseRedirect("/accounts/validate/")
				return response
			else:
				error = 'Something Went Wrong'
			return HttpResponseRedirect('/accounts/register/')
		else:
			user = User.objects.create_user(username= username, password=username)
			validationCode = generate_random_token()
			AppUser.objects.create(user=user, validationCode=validationCode)
			conn = SendSMS(username, validationCode)
			connection_status = conn.text
			status = {'status_code' : '200' , 'conn' : connection_status }
			user = authenticate(username=username, password=username)
			if user:
				login(request, user)
				response = HttpResponseRedirect("/accounts/validate/")
				return response
			else:
				error = 'Something Went Wrong'
			return HttpResponseRedirect('/accounts/register/')

	if request.method == 'GET':
		return render(request, 'register.html')


def validate_registration(request):
	if request.method == 'POST':
		validationCode = request.POST.get('validationCode')
		username = request.user.username
		user = User.objects.get(username=username)
		appUser = AppUser.objects.get(user=user)
		if appUser.validationCode == validationCode:
			appUser.validated = True
			appUser.save()
			response = HttpResponseRedirect('/accounts/register/complete/')
			return response
		else:
			wrong_token = 'کد وارد شده اشتباه است'
			return render(request, 'validation.html', {
				'error' : wrong_token
				})

	if request.method == 'GET':
		return render(request, 'validation.html')

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


def fullRegistration(request):
	if request.method == 'GET':
		return render(request, 'fullregistration.html')

	if request.method == 'POST':
		try:
			picture = request.FILES.get('profilePicture')
			username = request.user.username
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
			appUser.nationalID = request.POST['nationalID']
			appUser.save()
			state = request.POST['state']
			city = request.POST['city']
			phoneNumber = request.POST['phoneNumber']
			address = request.POST['address']
			postalCode = request.POST['postalCode']
			userAddress = Address.objects.create(appUser=appUser,state=state, phoneNumber=phoneNumber, 
				city=city,address=address, postalCode=postalCode)
			email = request.POST['email']
			sendMail(email, username)
			user.email = email
			user.save()
			return HttpResponseRedirect('/accounts/register/upline/')
		except IntegrityError:
			error = 'شما قبلا ثبت نام کرده اید.'
			return render(request, 'fullRegistration.html',{
				'error': error
				})

def parentObject(request):
	if request.method == 'POST':
		parentUsername = request.POST['parentUsername']
		parentUser = User.objects.filter(username=parentUsername)
		if parentUser:
			parent = AppUser.objects.get(user=parentUser)
			childUser = request.user
			child = AppUser.objects.get(user=childUser)
			ParentHood.objects.create(parent=parent, child=child)
			response = HttpResponseRedirect('/accounts/login/')
			success = 'درخواست شما برای آپلاین فرستاده شد، منتظر تایید بمانید.'
			return render(request, 'uplineRegister.html', {
				'success' : success
				})
		else:
			error = 'شماره وارد شده موجود نمیباشد.'
			return render(request, 'uplineRegister.html', {
				'error':error
				})
	if request.method == 'GET':
		return render(request, 'uplineRegister.html')


def mainPage(request):
	appUser = AppUser.objects.get(user=request.user)
	parenthood = ParentHood.objects.filter(child=appUser)
	return render(request, 'mainpage.html', {
		'appUser' : appUser, 'parenthood' : parenthood
		})

def profilepage(request):
	appUser = AppUser.objects.get(user=request.user)
	parenthood = ParentHood.objects.get(child=appUser)
	parent = parenthood.parent
	return render(request, 'profile.html', {
		'appUser' : appUser, 'parenthood' : parenthood, 'parent' : parent
		})

def notifications(request):
	appUser = AppUser.objects.get(user=request.user)
	parenthood = ParentHood.objects.filter(parent=appUser)
	return render(request, 'notifications.html', {
		'appUser' : appUser, 'parenthood' : parenthood
		})

def parentValidation(request):
	if request.method == 'GET':
		status = request.GET.get('status')
		childUsername = request.GET.get('cu')
		childUser = User.objects.get(username=childUsername)
		child = AppUser.objects.get(user=childUser)
		parentobj = request.user
		parent = AppUser.objects.get(user=parentobj)
		parenthood = ParentHood.objects.get(child=child, parent=parent)
		parenthood.validatedByParent = status
		parenthood.save()
		return HttpResponseRedirect('/accounts/main/notifs/')


def tasklist(request):
	if request.method == 'GET':
		user = request.user
		tasks = Task.objects.all().order_by('number')
		tasks = list(tasks)
		userSchedule = Scheduler.objects.filter(user=AppUser.objects.get(user=user))
		for schedule in userSchedule:
			if schedule.accomplished == True:
				if schedule.accepted == 'accepted' or schedule.accepted == 'pending':
					tasks.remove(schedule.task)
		return render(request, 'tasks.html', {
			'tasks':tasks , 'userSchedule' : userSchedule
			})


def taskaccomplished(request):
	if request.method == 'GET':
		username = request.GET.get('username')
		tasknumber = request.GET.get('tasknum')
		task = Task.objects.get(number=tasknumber)
		appUser = AppUser.objects.get(user=request.user)
		Scheduler.objects.create(user=appUser, task=task, accomplished=True)
		return HttpResponseRedirect('/accounts/tasks/')


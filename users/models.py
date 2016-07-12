from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AppUser(models.Model):
	roles = (('q' , 'qualify'), ('b' , 'bronze'), ('silver', 'silver'), ('g','gold'), ('p', 'platinium'))
	genderChoices = (('m','Male'), ('f','Female'))
	user = models.ForeignKey(User,
		verbose_name='User')
	profilePicture = models.ImageField(upload_to="user_images/" , null=True , blank= True, verbose_name='Avatar')
	validationCode = models.CharField(blank=True, null=True, max_length=5,
		verbose_name='Validation Code')
	validated = models.BooleanField(default=False, verbose_name='Is Mobile Phone Validated?')
	emailValidated = models.BooleanField(default=False, verbose_name='Is Email Validated?')
	mailToken = models.CharField(blank=True, null=False, max_length=20, verbose_name='Email Token')
	name = models.CharField(blank=True, null=True, max_length=100, verbose_name='Name')
	familyName = models.CharField(blank=True, null=True, max_length=100, verbose_name='Family Name')
	fatherName = models.CharField(blank=True, null=True, max_length=100, verbose_name='Father Name') 
	birthID = models.IntegerField(blank=True,null=True, verbose_name='Birth Certificate ID')
	birthDay = models.IntegerField(blank=True, null=True, verbose_name='Birth Day')
	birthMonth = models.IntegerField(blank=True, null=True, verbose_name='Birth Month')
	birthYear = models.IntegerField(blank=True, null=True, verbose_name='Birth Year')
	gender = models.CharField(blank=True, null=True, max_length=1, choices=genderChoices,verbose_name='Gender')
	nationalID = models.IntegerField(blank=True, null=True, verbose_name='National ID')
	role = models.CharField(max_length=20, blank=True, null=True, choices=roles)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = 'MLM User'
		verbose_name_plural = 'MLM Users'


class Address(models.Model):
	appUser = models.ForeignKey(AppUser, 
		verbose_name='App User')
	state = models.CharField(max_length=100, blank=True, null=True, 
		verbose_name='State')
	city = models.CharField(max_length=100, blank=True, null=True, verbose_name='City')
	address = models.TextField(verbose_name='Address')
	phoneNumber = models.IntegerField(blank=True,null='True',
		verbose_name='Mobile Phone Number', unique=True)
	mobileNumber = models.IntegerField(blank=True, null=True, verbose_name='Mobile Number')
	postalCode = models.IntegerField(blank=True, null=True, verbose_name='Postal Code')

	
	def __str__(self):
		return self.appUser.user.username

	class Meta:
		verbose_name_plural = 'Adresses'


class ParentHood(models.Model):
	validChoice = (('accepted' , 'Accepted'),
		('pending' , 'Pending'),
		('denied' , 'Denied'))

	parent = models.ForeignKey(AppUser, related_name='Parent',
		verbose_name='Parent')
	child = models.ForeignKey(AppUser, related_name='Child',
		verbose_name='Child')
	validatedByParent = models.CharField(default='pending', choices=validChoice, 
		max_length=10, verbose_name='Has Upline Validated?')

	def __str__(self):
		return self.parent.user.username

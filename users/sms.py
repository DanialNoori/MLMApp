#sending SMS
import requests
import random
import string

def generate_random_token():
    return ''.join(random.SystemRandom().choice(string.digits) for _ in range(5))


def SendSMS(PhoneNumber, validationCode):
	mobile = PhoneNumber
	text = 'کد فعال سازی شما در خانواده کارآفرین:\n'
	text += validationCode
	connection = requests.get('https://sms.payamgah.net/API/SendSms.ashx?username=milad&password=miladam&from=3000747717&'
	 + 'to=' + mobile + '&text=' + text, verify=False)
	return connection

from copy import copy
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
import requests as req
import json

# Create your views here.


TOKEN = 'fca_live_uT7BfNNzeDngCvYacGha2PwlIt2TMqHUonOfjOTr'
URL = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_uT7BfNNzeDngCvYacGha2PwlIt2TMqHUonOfjOTr'


def index(requests):
	response = req.get(URL, TOKEN).json()
	currency = response.get('data')

	if requests.method == 'GET':
		context = {'req': currency}
		#print(context)
		return render(requests, 'currency_templates/index.html',  context=context)
	

	if requests.method == 'POST':
		count_many = requests.POST.get('count_many')
		give = requests.POST.get('give')
		accept = requests.POST.get('accept')


		if count_many and give and accept:
			item = round(currency[accept] / currency[give] * float(count_many), 2)
		elif not give or not accept:
			item = 'Вы не выбралю валюту [!]'
		else:
			item = 'Введите сумму для конвертации [!]'

		context = {
		 	'req': currency,
		 	'item': item,
		 	'give': give,
		 	'accept': accept
		 	}
		#context = copy(context_new)
		#return HttpResponseRedirect()
		#context['item'] = item
		#context['give'] = give
		#context['accept'] = accept
#		
		#return HttpResponseRedirect('/', kwargs= {'req': currency,'item': item,'give': give,'accept': accept})
		#return redirect('/')
		
		return render(requests, 'currency_templates/index.html',  context=context)
		








from django.shortcuts import render
from django.http import HttpResponse, Http404
from django_daraja.mpesa.core import MpesaClient 
import requests
from requests.auth import HTTPBasicAuth
from siteworks import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
import asyncio
from core.models import Job,User

def reg_callback(request):
   url='https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'
   shortcode=settings.MPESA_SHORTCODE
   regurl='http://172.16.99.44:8000/callback'
   body={    
   "ShortCode": shortcode,
   "ResponseType":"Completed",
   "ConfirmationURL":regurl,
   'ValidationURL':regurl}
   headers={
      'Authorization':'Bearer EVLRvGHKNSvbK0YfgAbA7gYqqj7L',
      'Content-type':'application/json' }
   response=requests.post(url=url,headers=headers,data=body)
   return HttpResponse(response)

def auth_token():
  url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
  
  res=requests.get(url,auth=HTTPBasicAuth('fK7TnqdWkc8AztAKGUGPBYSlQ3AH8o7nPkqRPDOENSzFIrT8',
      '32rotjNmHNwh0hq1z0jQfmdJiAOBXArg4MxkTiDFLA5AbrLetjsNtVDm7osp9CiK'))
  token=res.json()['access_token']
  return 'Bearer'+token


def ni_push(request):
   url='https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'
   headers={
      'Authorization':auth_token(),
      'Content-type':'application/json'
   }
   res=request.post()

def index(tel,amount):
    client = MpesaClient()
    phone_number = tel
    amount = amount
    account_reference = 'Austine'
    transaction_desc = 'Payment'
    callback_url = 'http://172.16.98.55:8000/callback'
    response = client.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

@receiver(post_save,sender=Job)
async def initiate_payment(sender,instance,created,**kwargs):
   if created:
      await asyncio.sleep(5)  #awaits 5 seconds before payment initiation
      index(instance.telephone,instance.budget)
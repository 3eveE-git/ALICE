#Google Fact Checker
#This program uses Google's native fact chec key API and returns the turth value based on ALICE. This module is an auxlillary to the main BERT and GPT3.

from xml.sax.xmlreader import AttributesImpl
import requests
import json 

querystr = input('Please enter the query :\n')

parameters = {
    "query": querystr,
    "languageCode": "eng",
    "maxAgeDays" :60,
    "key" : "AIzaSyBHU_ic4FPPateUq8f7umlJ3lg1mb7FDFA"
}

response = requests.get("https://factchecktools.googleapis.com/v1alpha1/claims:search?", params= parameters)

#print(response.json())

response_converted_to_json = response.json()
print(response_converted_to_json['claims'][0]['claimReview'][0]['textualRating'])

#ratedtext = response_converted_to_json['claims'][0]['claimReview'][0]['textualRating']









 
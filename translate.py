#Language Support
#This program would give the english translation of any query that is from another language. 
#The language detection modules are from Google. Written for project ALICE. This program also takes in string input, this would need to take the query for ALICE as input.
#This program also needs a paid API account key. 


import requests
import json
import six
from google import cloud
from google.cloud import translate_v2 as translate

querystr = input('Please enter text to be translated: \n')

parameters ={
    "q": querystr,
    "target" : "en",
    "key" : "AIzaSyBHU_ic4FPPateUq8f7umlJ3lg1mb7FDFA"
}

#Translating to English
response = requests.get("https://translation.googleapis.com/language/translate/v2", params = parameters)
response_converted_to_json = response.json()


if response_converted_to_json['data']['translations'][0]['detectedSourceLanguage'] == 'und':
    print("Language undetected")

else:
    print("Here is the translation: \n")
    print(response_converted_to_json['data']['translations'][0]['translatedText'])




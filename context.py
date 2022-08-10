# Context
# This program returns 3 files (articles) from NY Time adn Guardian each to give a more wholesome understanding of the topic on which the query is based.


from xml.sax.xmlreader import AttributesImpl
import requests
import json
from datetime import datetime 
from datetime import timedelta


querystr = input("Please enter lookup query: \n")

#Limiting the date of article to 60 before current time; 
edate = datetime.date(datetime.now())
d = timedelta(days =60)
bdate = edate - d

print()
print()

# NY TIMES 
nyparameters = {
    "q" : querystr,
    "document_type" : "article",
    "begin_date" : bdate,
    "end_date" : edate,
    "sort" : "relevance",
    "api-key" : ""  #Add NY Times API key
}

response = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json?", params = nyparameters)
#print(response.json())

nytimes_response_json = response.json()



# GUARDIAN Article
gparameters = {
    "q" : querystr,
    "format" : "json",
    "lang" : "en",
    "from-date" : bdate,
    "to-date" : edate,
    "order-by" : "relevance",
    "api-key" : ""  #Add the Guardian API Keys

}

response = requests.get("https://content.guardianapis.com/search", params = gparameters)
#print(greponse.json())

g_response_json = response.json()



#Printing relevant response: First 3 articles from each publication, in the last 60 days. Article Title, URL.

print("Related Articles: The NY Times")
c1 = 0
while (c1<3):
    c1 = c1 + 1
    print(nytimes_response_json['response']['docs'][c1]['abstract'])
    print(nytimes_response_json['response']['docs'][c1]['web_url'])

print()
print()
print("Related Articles: The Guardian")    
c2 = 0
while (c2<3):
    c2 = c2 + 1
    print(g_response_json['response']['results'][c2]['webTitle'])
    print(g_response_json['response']['results'][c2]['webUrl'])
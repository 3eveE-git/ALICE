# ALICE
ALICE- Analytical Language Interpretation and Classification Environment

This is project created in collaboration with the IDeaS Center CMU, under the guidance of Dr. Kathleen Carley. Contributors include Prakhar Agrawal, Alice Xinran Ma and Lily Junyi Guo.

ALICE is an ML system that encapsulates NLP models (BERT and GPT3) to assess the accuracy parameters of statements input by the user. It was created to be a multiprong effort to combat misinforamtion in social media.

Main Project Repos:

Web Server:  https://github.com/prakhariitd/ALICE

Plug In: https://github.com/xrma99/ALICE_plugin


This module (repo) of the ALICE is for future development and tangential fucntions of the project.

Modules contained in this repo:
- Google Fact Checker: GFC is a Google based system that is a database of manually classified data. This can be added to the project to increase the accuracy of the ML systems. This program would take in a text and return the classification along with the probablity. Avaiable in two files, newgfc.py- would return the textual rating for the text and gfcresult.py - would return the numerical value for any textual rating.

- Translation: This program would detect another language and translate it to English as ALICE currently only supports English. This program would increase the language range of the project. This needs Google API credits.

- Context: This module uses NY Times and The Guardian news agencies to fetch 3 news articles that would help the user of ALICE understand more about the topic queried. This is to help reduce information loss.


Other Suggested Advancements:
- Google SSO
- Source Tracking for Twitter

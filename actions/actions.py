import requests
import bs4
import urllib

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class Fact_Checker(Action):
    def name(self) -> Text:
        return "action_fact_check"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text= tracker.get_slot("Event_check")
        url = 'https://google.com/search?q=' + text
        request_result = requests.get( url )
        soup = bs4.BeautifulSoup( request_result.text 
                         , "html.parser" )
        temp = soup.find( "div" , class_='BNeawe' ).text 
    
        print( temp )
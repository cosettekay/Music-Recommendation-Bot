# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List            # required
from rasa_sdk import Action, Tracker                # required
from rasa_sdk.executor import CollectingDispatcher  # required
import requests
import json

API_KEY = '230c9a1f8bcf18057ae9777fde25517c'
USER_AGENT = 'HELPME'

def lastfm_get(payload):
    headers = {
        'user-agent': USER_AGENT
    }
    url = 'http://ws.audioscrobbler.com/2.0/'
    payload['api_key'] = API_KEY
    payload['format'] = 'json'
    response = requests.get(url, headers=headers, params=payload)
    return response

class ActionGetEmotionTags(Action):

    def name(self) -> Text:
        return "action_get_emotion_tags"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        emotions = ['happy', 'sad', 'angry', 'calm', 'relaxed', 'excited', 'emotional']

        for emotion in emotions:
            response = lastfm_get({
                'method': 'tag.getTopTracks',
                'tag': emotion,
                'limit': 10
            })
            if response.status_code == 200:
                dispatcher.utter_message(text=f'Top Tracks for {emotion}:')
                for track in response.json()['tracks']['track']:
                    dispatcher.utter_message(text=f"{track['name']} by {track['artist']['name']}. URL: {track['url']} \n")
            else:
                dispatcher.utter_message(text=f'Error occured: {response.status_code}')
                
        return []


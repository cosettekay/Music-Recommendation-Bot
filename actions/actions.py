# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List            # required
from rasa_sdk import Action, Tracker                # required
from rasa_sdk.events import Restarted
from rasa_sdk.executor import CollectingDispatcher  # required

import requests
import json
import random

API_KEY = 'enter your Last.FM API'
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

class ActionGetEmotionTracks(Action):

    emotion = None
    
    def name(self) -> Text:
        return "action_get_emotion_tracks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        response = lastfm_get({
            'method': 'tag.getTopTracks',
            'tag': self.emotion,
            'limit': 10
        })
        if response.status_code == 200:
            dispatcher.utter_message(text=f'Top Tracks for {self.emotion}:')
            for track in response.json()['tracks']['track']:
                dispatcher.utter_message(text=f"{track['name']} by {track['artist']['name']}. URL: {track['url']} \n")
        else:
            dispatcher.utter_message(text=f'Error occured: {response.status_code}')
                
        return []


class ActionGetHappyTracks(ActionGetEmotionTracks):
    emotion = 'happy'
    
    def name(self) -> Text:
        return "action_get_happy_tracks"

class ActionGetSadTracks(ActionGetEmotionTracks):
    emotion = 'sad'
    
    def name(self) -> Text:
        return "action_get_sad_tracks"

class ActionGetAngryTracks(ActionGetEmotionTracks):
    emotion = 'angry'
    
    def name(self) -> Text:
        return "action_get_angry_tracks"
    
class ActionGetCalmTracks(ActionGetEmotionTracks):
    emotion = 'calm'
    
    def name(self) -> Text:
        return "action_get_calm_tracks"
    
class ActionGetRelaxedTracks(ActionGetEmotionTracks):
    emotion = 'relaxed'
    
    def name(self) -> Text:
        return "action_get_relaxed_tracks"

class ActionGetExcitedTracks(ActionGetEmotionTracks):
    emotion = 'excited'
    
    def name(self) -> Text:
        return "action_get_excited_tracks"
    
class ActionGetEmotionalTracks(ActionGetEmotionTracks):
    emotion = 'emotional'
    
    def name(self) -> Text:
        return "action_get_emotional_tracks"
    
class ActionGetRandomTracks(Action):
    
    emotion = None
    
    def name(self) -> Text:
        return "action_get_random_tracks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        response = lastfm_get({
            'method': 'tag.getTopTracks',
            'tag': self.emotion,
            'limit': 100
        })
        if response.status_code == 200:
            tracks = response.json()['tracks']['track']
            random_tracks = random.sample(tracks, 5)
            dispatcher.utter_message(text=f'Random Tracks for {self.emotion}:')
            for track in random_tracks:
                dispatcher.utter_message(text=f"{track['name']} by {track['artist']['name']}. URL: {track['url']} \n")
        else:
            dispatcher.utter_message(text=f'Error occured: {response.status_code}')
                
        return [Restarted()]
    
class ActionGetRandHappyTrack(ActionGetRandomTracks):
    emotion = 'happy'
    
    def name(self) -> Text:
        return "action_get_randHappy_tracks"
    
class ActionGetRandSadTrack(ActionGetRandomTracks):
    emotion = 'sad'
    
    def name(self) -> Text:
        return "action_get_randSad_tracks"

class ActionGetRandAngryTrack(ActionGetRandomTracks):
    emotion = 'angry'
    
    def name(self) -> Text:
        return "action_get_randAngry_tracks"
    
class ActionGetRandRelaxedTrack(ActionGetRandomTracks):
    emotion = 'relaxed'
    
    def name(self) -> Text:
        return "action_get_randRelaxed_tracks"
    
class ActionGetRandExcitedTrack(ActionGetRandomTracks):
    emotion = 'excited'
    
    def name(self) -> Text:
        return "action_get_randExcited_tracks"

class ActionGetRandEmotionalTrack(ActionGetRandomTracks):
    emotion = 'emotional'
    
    def name(self) -> Text:
        return "action_get_randEmotional_tracks"
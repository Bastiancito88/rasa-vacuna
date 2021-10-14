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
class ActionContraindicaciones(Action):
    
    def name(self) -> Text:
        return "action_contraindicaciones_todas"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             
             
        #entities = tracker.entities
        #intentd = tracker.intetns

        list_of_entities = tracker.latest_message['entities']
        vacuna_joint = set(['bcg', 'vph', 'dtpa'])
        topic_joint = set(['contraindicacion'])

        topic = topic_joint.intersection(set(list_of_entities))
        vacuna = vacuna_joint.intersection(set(list_of_entities))
        
        empty_vacuna = (len(vacuna) == 0)
        empty_topic = (len(topic) == 0)

        if not(empty_vacuna) and not(empty_topic):
            
            dispatcher.utter_message(response = "utter_"+ str(topic) + "_" + str(vacuna) )
        else:
            print('pase por la excepcion ')
            dispatcher.utter_message(text ="action not found")    

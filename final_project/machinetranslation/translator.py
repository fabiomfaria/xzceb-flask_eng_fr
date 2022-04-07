""" Tradutor de texto do En-Fr e Fr-En """
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('url')

def english_to_french(english_text):
    """ Função de Tradução do Inglês para o Francês """
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    #french_text=json.dumps(translation, indent=2, ensure_ascii=False)
    french_text=translation
    return french_text

def french_to_english(french_text):
    """ Função de Tradução do Francês para o Inglês """
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text=translation
    #json.dumps(translation, indent=2, ensure_ascii=False)
    return english_text

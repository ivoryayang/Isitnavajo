from google.cloud import translate_v2 as translate
import logging
import time

def create_client():
    return translate.Client()

def detect_language(client, text):
    try:
        response = client.detect_language(text)
        return response['language'], response['confidence']
    except Exception as e:
        logging.error(f"Error detecting language: {str(e)}")
        return None, None

def batch_detect_languages(client, sentences):
    languages = []
    for sentence in sentences:
        language, confidence = detect_language(client, sentence)
        if language:
            languages.append((language, confidence))
        else:
            languages.append(('unknown', 0))
    return languages

def translate_text(client, text, target_language, source_language):
    try:
        result = client.translate(text, source_language=source_language, target_language=target_language)
        return result['translatedText']
    except Exception as e:
        logging.error(f"Failed to translate text from {source_language} to {target_language}: {str(e)}")
        return None

def translate_round_trip(client, text, source_language):
    if source_language == 'en':
        return text, text
    translated_to_english = translate_text(client, text, 'en', source_language)
    translated_back = translate_text(client, translated_to_english, source_language, 'en')
    return translated_to_english, translated_back

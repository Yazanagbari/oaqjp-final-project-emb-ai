# emotion_detection.py
import requests
import json

def emotion_detector(text_to_analyze):
    """
    This function sends the text to the Watson NLP Emotion Predict function
    and returns the entire response JSON.
    """
    # Check for empty string first to avoid unnecessary request
    if not text_to_analyze.strip():
        return None
        
    # The URL, headers, and input JSON as provided
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Send the POST request
    response = requests.post(url, json=input_json, headers=headers)
    
    # Return the response JSON. We will format this output in the next task.
    return response.text

 
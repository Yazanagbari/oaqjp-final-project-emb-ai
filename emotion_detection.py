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
    
     # Convert the response text to a Python dictionary
    response_dict = json.loads(response.text)
    
    # Extract the emotion scores from the nested structure
    emotions = response_dict['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Find the dominant emotion (the key with the maximum value)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    

 
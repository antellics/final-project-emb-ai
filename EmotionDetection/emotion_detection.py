#!/usr/bin/env python3.11
"""
Emotion detection
"""
import json
import requests

def emotion_detector(text_to_analyse: str) -> dict:
    """
    Interface to IBM NLP libraries
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/"\
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    if response.status_code == 400:
        anger_score = disgust_score = fear_score = joy_score = sadness_score = dominant_emotion = None
        return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        }
    formatted_response = json.loads(response.text)
    if formatted_response.get("emotionPredictions"):
        emotions = formatted_response.get("emotionPredictions")[0].get("emotion")
        anger_score = emotions.get("anger")
        disgust_score = emotions.get("disgust")
        fear_score = emotions.get("fear")
        joy_score = emotions.get("joy")
        sadness_score = emotions.get("sadness")
        dominant_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)
        if anger_score == dominant_score:
            dominant_emotion = 'anger'
        elif disgust_score == dominant_score:
            dominant_emotion = 'disgust'
        elif fear_score == dominant_score:
            dominant_emotion = 'fear'
        elif joy_score == dominant_score:
            dominant_emotion = 'joy'
        else:
            dominant_emotion = 'sadness'
        return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
                }

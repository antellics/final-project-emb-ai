#!/usr/bin/env python3.11
"""
emotionDetector server component
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Call to NLP tools
    """
    result = emotion_detector(request.args.get("textToAnalyze"))
    if result.get('dominant_emotion') is None:
        return "Invalid input ! Try again."
    else:
        response_text = "For the given statement, the system response is "
        response_text += f"'anger': {result.get('anger')}, "
        response_text += f"'disgust': {result.get('disgust')}, "
        response_text += f"'fear': {result.get('fear')}, "
        response_text += f"'joy': {result.get('joy')} and "
        response_text += f"'sadness': {result.get('sadness')}. "
        response_text += f"The dominant emotion is <b>{result.get('dominant_emotion')}</b>."
    
        return response_text


@app.route("/")
def render_index_page():
    """
    Default route
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

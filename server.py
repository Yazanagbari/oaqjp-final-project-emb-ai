
from flask import Flask, request, jsonify, render_template 
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Endpoint to analyze emotion from provided text.
    Expects a 'text' query parameter.
    Returns a formatted string response.
    """
    # Get the text from the query parameter
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Analyze the emotion
    result = emotion_detector(text_to_analyze)
    
    # Format the response string as required
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <strong>{result['dominant_emotion']}</strong>."
    )
    return response_text

@app.route("/")
def index():
    """Serves the main index.html page from the templates folder."""
    return render_template('index.html')  # <-- This requires the import

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
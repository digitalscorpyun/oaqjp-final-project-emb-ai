from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    text_to_analyze = request.form["text"]
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return render_template("index.html", output="Invalid text! Please try again!")

    formatted_response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return render_template("index.html", output=formatted_response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

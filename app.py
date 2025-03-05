# app.py
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load pre-trained summarization model
summarizer = pipeline('summarization')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)

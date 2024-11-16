import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', bio=None)

@app.route('/generate', methods=['POST'])
def generate():
    # Parse JSON data from the request
    data = request.get_json()
    career = data.get('career', 'Unknown career')
    personality = data.get('personality', 'Unknown personality')
    interests = data.get('interests', [])

    # Generate the bio (replace this with OpenAI logic if needed)
    bio = generate_bio(career, personality, interests)
    return jsonify({"bio": bio})

def generate_bio(career, personality, interests):
    # Simple logic for bio generation
    interests_str = ", ".join(interests) if interests else "varied interests"
    return f"A {personality} {career} with a passion for {interests_str}."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)

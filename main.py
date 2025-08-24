from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        text = data.get('text', '')
        src = data.get('src', '')
        dest = data.get('dest', '')

        translated = GoogleTranslator(source=src, target=dest).translate(text)
        return jsonify({'translated_text': translated})
    except Exception as e:
        return jsonify({'error': 'Translation failed', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

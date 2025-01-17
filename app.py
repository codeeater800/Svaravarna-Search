from flask import Flask, render_template, request, jsonify
from indic_transliteration import sanscript

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/transliterate', methods=['POST'])
def transliterate():
    data = request.get_json()
    text_to_transliterate = data['text']

    transliterated_text = sanscript.transliterate(text_to_transliterate, sanscript.IAST, sanscript.DEVANAGARI)

    return jsonify({'transliteratedText': transliterated_text})

if __name__ == "__main__":
    app.run(debug=True)

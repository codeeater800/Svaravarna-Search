from flask import Flask, request, jsonify, send_from_directory
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import os

app = Flask(__name__, static_folder='public')

# Serve static files (HTML, CSS, etc.)
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# API endpoint for transliteration
@app.route('/api/transliterate', methods=['POST'])
def transliterate_text():
    data = request.json
    text = data.get('text')
    source_script = data.get('source_script')
    target_script = data.get('target_script')

    if not text or not source_script or not target_script:
        return jsonify({'error': 'Missing required fields: text, source_script, target_script.'}), 400

    # Map script names to sanscript constants
    script_map = {
        'devanagari': sanscript.DEVANAGARI,
        'iast': sanscript.IAST,
    }

    source = script_map.get(source_script.lower())
    target = script_map.get(target_script.lower())

    if not source or not target:
        return jsonify({'error': 'Invalid source_script or target_script.'}), 400

    transliterated_text = transliterate(text, source, target)
    return jsonify({'transliterated_text': transliterated_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

import json
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def handler(request, context):
    if request.method != 'POST':
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed. Use POST.'})
        }

    try:
        data = request.json
        text = data.get('text')
        source_script = data.get('source_script')
        target_script = data.get('target_script')

        if not text or not source_script or not target_script:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing required fields: text, source_script, target_script.'})
            }

        # Map script names to sanscript constants
        script_map = {
            'devanagari': sanscript.DEVANAGARI,
            'iast': sanscript.IAST,
            # Add more mappings if needed
        }

        source = script_map.get(source_script.lower())
        target = script_map.get(target_script.lower())

        if not source or not target:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid source_script or target_script.'})
            }

        transliterated_text = transliterate(text, source, target)

        return {
            'statusCode': 200,
            'body': json.dumps({'transliterated_text': transliterated_text})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

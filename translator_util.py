import json
from googletrans import Translator

translator = Translator()
LANGUAGES = ['en']


def translate_text(text, dest_language='en'):
    try:
        src_lang = translator.detect(text).lang
        if src_lang != dest_language:
            return translator.translate(text, src=src_lang, dest=dest_language).text
        return text
    except Exception as e:
        return text


def translate_json_values(json_data, dest_language='en'):
    for key in json_data:
        if isinstance(json_data[key], str):
            json_data[key] = translate_text(json_data[key], dest_language)
    return json_data


def translate_lang_json(lang: str = "ru"):
    json_filename = f'i18n/{lang}.json'
    try:
        with open(json_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    
    translated_data = translate_json_values(data, dest_language=lang)

    with open(json_filename, 'w', encoding='utf-8') as file:
        json.dump(translated_data, file, indent=2, ensure_ascii=False)


translate_lang_json(lang="kk")
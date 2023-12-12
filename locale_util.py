import os
import json
import datetime

LANGUAGES = ['ru', 'kk', 'en']
cur_path = f"i18n/{datetime.datetime.now()}"


def update_lang_json(translations: dict, lang: str = "ru"):
    if not os.path.exists(cur_path):
        os.makedirs(cur_path)

    json_filename = os.path.join(cur_path, f'{lang}.json')
    try:
        with open(json_filename, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = {}

    existing_data.update({key: value for key, value in translations.items()})

    with open(json_filename, 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, indent=2, ensure_ascii=False)


def update_languages(translations: dict, languages: list = LANGUAGES):
    for lang in languages:
        update_lang_json(translations, lang=lang)
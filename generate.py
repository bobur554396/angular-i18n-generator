import os
import argparse
import glob
import re
from translit_util import gen_trans
from locale_util import update_languages


def process_html_file(file_path: str, translations: dict):

    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    def replace_russian_text(match):
        text = match.group(1).strip()
        if re.search(r'[\u0400-\u04FF]+', text):
            key = gen_trans(text.strip().replace(' ', '_').lower())
            translations[key] = text.strip()
            return '>{{ "' + key + '" | translate }}</'
        return match.group(0)


    cyrillic_pattern = re.compile(r'>([^<>]+)</')
    updated_html_content = cyrillic_pattern.sub(replace_russian_text, html_content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_html_content)


def update_all_html_files(src_directory: str):
    translations = dict()
    html_files = glob.glob(os.path.join(src_directory, '**/*.html'), recursive=True)

    for file_path in html_files:
        process_html_file(file_path, translations)

    update_languages(translations=translations)
    return translations



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Angular HTML files for translation keys.")
    parser.add_argument("project_root", type=str, help="Path to the Angular project root directory")

    args = parser.parse_args()

    angular_project_root = args.project_root
    app_directory = os.path.join(angular_project_root, 'src', 'app')
    translations = update_all_html_files(app_directory)
    print(translations)



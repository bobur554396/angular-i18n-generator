import re
from transliterate import translit


def gen_trans(_value):
    _value = str(_value)
    _value = re.sub(r'\s+', '_', _value)
    _trans = translit(re.sub(r'\W+', '', _value), 'ru', reversed=True).replace('\'', '')
    return '_'.join([val.lower() for val in _trans.split(' ')])



# print(gen_trans("Введите пароль"))
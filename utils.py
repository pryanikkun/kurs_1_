import requests
import json
import random
import basicwords

DATA_SOURCE = 'https://www.jsonkeeper.com/b/WFKH'


def load_random_word():
    """
    - получает список слов с внешнего ресурса
    - выбирает случайное слово
    - создает экземпляр класса BasicWord
    :return: экземпляр класса BasicWord
    """

    # получим список слов с внешнего ресурса
    file = requests.get(DATA_SOURCE)
    list_file = json.loads(file.text)

    # получим случайное слово
    random_dict = random.choice(list_file)
    origin_word = random_dict['word']
    subwords = random_dict['subwords']

    # создаём экземпляр класса BasicWord
    word = basicwords.BasicWord(origin_word, subwords)

    return word

class Player:
    def __init__(self, name, using_words):
        self.name = name
        self.using_words = using_words

    def count_using_words(self):
        """
        Получение количества использованных слов
        :return: int
        """
        return len(self.using_words)

    def add_word_in_using_words(self, new_word):
        """
        Добавление слова в использованные слова
        :return: nothing
        """
        self.using_words.append(new_word)

    def is_using_word(self, new_word):
        """
        Проверка использования слова до этого момента жизни
        :return: bool
        """
        return new_word in self.using_words

    def __repr__(self):
        return f'Игрок {self.name}. Список использованных слов {self.using_words}'

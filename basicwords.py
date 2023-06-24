class BasicWord:
    def __init__(self, original_word, list_subwords):
        self.original_word = original_word
        self.list_subwords = list_subwords

    def is_in_set_words(self, player_word):
        """
        Проверка введенного слова в списке допустимых подслов
        :return: bool
        """
        return player_word in self.list_subwords

    def count_subwords(self):
        """
        Подсчет количества подслов
        :return: int
        """
        return len(self.list_subwords)

    def __repr__(self):
        return f"Слово {self.original_word}, список подслов {self.list_subwords}"

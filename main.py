import utils
import player

user_name = input('Введите имя игрока\n')
player = player.Player(user_name, [])
print(f'Привет, {player.name}!')

word = utils.load_random_word()
count_subwords = word.count_subwords()

print(f'Составьте {count_subwords} слов из слова {word.original_word}\n'
      'Слова должны быть не короче 3 букв\n'
      'Чтобы закончить игру, угадайте все слова или напишите "stop"\n'
      'Поехали, ваше первое слово?')

while player.count_using_words() < count_subwords:
    user_try = input()
    if (user_try == "stop") | (user_try == "стоп"):
        break
    elif len(user_try) < 3:
        print("слишком короткое слово")
        continue
    elif player.is_using_word(user_try):
        print("уже использовано")
        continue
    elif not word.is_in_set_words(user_try):
        print("неверно")
        continue
    else:
        player.add_word_in_using_words(user_try)
        print('верно')

print(f'Игра завершена, вы угадали {len(player.using_words)}!')

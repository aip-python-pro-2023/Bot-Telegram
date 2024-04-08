import telebot
import random

bot = telebot.TeleBot('7132950816:AAHC3u4NBwtquEPDDB9-zhYkMGT1T5hs4Ic')

word_list = ["яблоко", "банан", "апельсин", "виноград", "ананас", "клубника", "киви", "арбуз", "персик", "манго",
             "вишня", "голубика", "абрикос", "груша", "слива", "лимон", "лайм", "кокос", "гранат", "инжир",
             "малина", "ежевика", "дыня", "нектарин", "мандарин", "хурма", "дыня", "авокадо",
             "гуава", "маракуйя", "личи", "питайя", "папайя", "шелковица", "клюква", "ежевика",
             "крыжовник", "годжи", "смородина", "черника", "брусника", "фейхоа", "инжир", "цитрон", "мушмула",
             "клементин", "малина", "черешня", "клюква", "фрукт", "виноград", "мандарин", "яблоко", "банан",
             "апельсин", "виноград", "ананас", "клубника", "киви", "арбуз", "персик", "манго",
             "вишня", "голубика", "абрикос", "груша", "слива", "лимон", "лайм", "кокос", "гранат", "инжир",
             "малина", "ежевика", "дыня", "нектарин", "мандарин", "хурма", "дыня", "авокадо",
             "гуава", "маракуйя", "личи", "питайя", "папайя", "шелковица", "клюква", "ежевика",
             "крыжовник", "годжи", "смородина", "черника", "брусника", "фейхоа", "инжир", "цитрон", "мушмула",
             "клементин", "малина", "черешня", "клюква", "фрукт", "виноград", "мандарин"]

MAX_ATTEMPTS = 6
MAX_HINTS = 3
hints_used = 0
attempts_left = MAX_ATTEMPTS
secret_word = ""
guessed_word = ""


@bot.message_handler(commands=['start'])
def start_message(message):
    global attempts_left
    global hints_used
    global secret_word
    global guessed_word

    attempts_left = MAX_ATTEMPTS
    hints_used = 0
    secret_word = random.choice(word_list)
    guessed_word = "_" * len(secret_word)

    word_length = len(secret_word)  # Получаем длину загаданного слова
    word_with_spaces = " ".join(guessed_word)  # Добавляем пробелы между подчеркиваниями

    bot.send_message(message.chat.id, "Привет! 😊")
    bot.send_message(message.chat.id,
                     f"Давай сыграем в игру 'Виселица'! Я загадал слово из {word_length} букв: {word_with_spaces}\n\n"
                     "Используй команды:\n"
                     "/hint - получить подсказку (можно использовать до 3 раз)\n"
                     "/start - начать новую игру")


@bot.message_handler(commands=['hint'])
def send_hint(message):
    global secret_word
    global guessed_word
    global hints_used

    if hints_used < MAX_HINTS:
        not_guessed = [letter for letter in secret_word if letter not in guessed_word]
        if not_guessed:
            hint = random.choice(not_guessed)
            bot.send_message(message.chat.id, f"Подсказка: буква '{hint}' есть в загаданном слове.")
            hints_used += 1
        else:
            bot.send_message(message.chat.id, "Все буквы уже угаданы.")
    else:
        bot.send_message(message.chat.id, "Вы использовали все доступные подсказки.")


@bot.message_handler(content_types=['text'])
def check_letter(message):
    global guessed_word
    global secret_word
    global attempts_left

    if attempts_left > 0:
        if len(message.text) == 1 and message.text.isalpha():
            letter = message.text.lower()

            if letter in secret_word:

                guessed_word = ''.join([char if char == letter or guessed_word[idx] != '_' else '_' for idx, char in
                                        enumerate(secret_word)])
                bot.send_message(message.chat.id, guessed_word)
                if guessed_word == secret_word:
                    bot.send_message(message.chat.id,
                                     "Поздравляю, ты угадал слово! Хочешь сыграть ещё раз? Напиши /start")
            else:
                bot.send_message(message.chat.id, f"Буквы '{letter}' нет в загаданном слове, попробуй ещё раз!")
                attempts_left -= 1
                bot.send_message(message.chat.id, f"У вас осталось {attempts_left} попыток.")
        else:
            bot.send_message(message.chat.id, "Пожалуйста, введите только одну букву.")
    else:
        bot.send_message(message.chat.id, "У вас закончились попытки. Хотите сыграть ещё раз? Напиши /start.")


bot.polling()

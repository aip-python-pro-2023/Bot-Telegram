# Bot-Telegram Виселица

Telegram Bot - @visilechagamesbot

# Импорт библиотеки и установка токена бота:

<code> import telebot
import random

bot = telebot.TeleBot('Токен моего бота')
</code>

Этот код импортирует необходимую библиотеку для работы нашего Telegram Бота.

# Список слов:

<code> word_list = ["яблоко", "банан", ... ] </code>


Этот список содержит слова, из которых будет случайным образом выбираться одно для угадывания.

# Настройки игры

<code>MAX_ATTEMPTS = 6
MAX_HINTS = 3
hints_used = 0
attempts_left = MAX_ATTEMPTS
secret_word = ""
guessed_word = ""</code>

Здесь определяются параметры игры: максимальное число попыток (MAX_ATTEMPTS), максимальное число подсказок (MAX_HINTS), а также переменные для отслеживания использованных подсказок, оставшихся попыток, загаданного слова и угаданного слова.

# Показ работы команды /start:

<code>@bot.message_handler(commands=['start'])
def start_message(message):
    global attempts_left
    global hints_used
    global secret_word
    global guessed_word 
    ...</code>


Когда пользователь отправляет команду /start, эта функция сбрасывает значения переменных, инициализирует загаданное слово и угаданное слово, а затем отправляет приветственное сообщение и инструкцию о том, как играть.

# Показ работы команды /hint:

<code>@bot.message_handler(commands=['hint'])
def send_hint(message):
    global secret_word
    global guessed_word
    global hints_used
    ...</code>

Эта функция вызывается, когда пользователь отправляет команду /hint. Она проверяет количество использованных подсказок и отправляет подсказку (если есть неугаданные буквы в слове).

# Обработка текстовых сообщений:

<code>@bot.message_handler(content_types=['text'])
def check_letter(message):
    global guessed_word
    global secret_word
    global attempts_left
    ...</code>
 
При вызове команды /hint пользователем данная функция проверяет количество использованных подсказок и отправляет неугаданные буквы в слове, если они есть.

# Запуск бота:

<code>bot.polling()</code>

Этот способ начинает отслеживать сообщения от Telegram и вызывает соответствующие обработчики для обработки команд и сообщений пользователей.

Таким образом, код показывает игру "Виселица" в Telegram, где бот загадывает слово, а пользователь должен угадать его, отправляя буквы. Пользователь может использовать команду /hint, чтобы получить подсказку, и бот отслеживает количество попыток и подсказок.

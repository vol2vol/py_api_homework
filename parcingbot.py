import sqlite3
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Создаем подключение к базе данных или создаем новую, если она не существует
conn = sqlite3.connect('mydata.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS blocks (name TEXT, description TEXT)''')
conn.close()

# Функция обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот. Напиши мне название материала, например Teplo max или и я поищу похожие в базе данных.')

# Функция обработки сообщений от пользователя
def echo(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text

    # Подключаемся к базе данных
    conn = sqlite3.connect('mydata.db')
    cursor = conn.cursor()
    
    # Ищем похожие слова в базе данных только по полю "name"
    cursor.execute("SELECT name, description FROM blocks WHERE name LIKE ?", ('%' + user_input + '%',))
    results = cursor.fetchall()
    
    if results:
        response = "Результаты по запросу '{}':\n".format(user_input)
        for row in results:
            response += f"Название: {row[0]}, Описание: {row[1]}\n"
    else:
        response = "К сожалению, ничего не найдено."

    update.message.reply_text(response)

    conn.close()

# Функция для запуска бота
def main() -> None:
    # Токен вашего бота
    token = '6953114686:AAEdUQYXKEJ61QRH6mItFoK7e_TIhXQUyj8'
    # Создаем обновление и диспетчер
    updater = Updater(token)
    dispatcher = updater.dispatcher

    # Добавляем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    # Добавляем обработчик для всех сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
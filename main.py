from telebot import TeleBot, types
import json

#создание бота
bot = TeleBot(token='6219647096:AAF2x922H7mOhEEd0Umf8rLILVWhSJjwgkI', parse_mode='html') # создание бота

#создание кнопок
buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

buttons.row(
    types.KeyboardButton(text='Узнать про Алекса'),
    types.KeyboardButton(text='Валидатор + бьютифаер JSON'),
)

#ответ на команду start
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Привет! Провалидировать JSON или рассказатьнемного о моем создателе?\nНажми на кнопку, соответствующую твоему желанию',
        reply_markup=buttons,
    )

#ответы на сообщение кнопок
@bot.message_handler()
def message_handler(message: types.Message):
    if message.text == 'Валидатор + бьютифаер JSON':

        bot.send_message(
            chat_id=message.chat.id,
            text= 'Введи JSON в виде строки\nНапример: {"name":"Alex"}',
        )

    elif message.text == 'Узнать про Алекса':
        #создание кнопки под сообщением
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Alex CV", url='https://alexmed-qa.github.io/')
        markup.add(button1)

        bot.send_message(
            chat_id=message.chat.id,
            text="Мой создатель очень позитивный, юморной и супер крутой человек. Ты можешь узнать о нем больше, перейдя на его сайт-визитку, нажав кнопку ниже. Надеюсь, тебе понравится)",
            reply_markup = markup
        )

    else:
        #пытаемся распарсить JSON    
        try:
            payload = json.loads(message.text)

        except json.JSONDecodeError as ex:
            bot.send_message(
                chat_id=message.chat.id,
                text=f'При обработке произошла ошибка:\n<code>{str(ex)}</code>'
            )
            
            return #выходим из функции
        
        text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
        
        bot.send_message(
            chat_id=message.chat.id,
            text=f'JSON:\n<code>{text}</code>'
        )

#постоянная работа бота
bot.polling(none_stop=True, interval=0)

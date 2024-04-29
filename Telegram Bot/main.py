import telebot
import random
from telebot import types

# Conexion con nuestro BOT
TOKEN = 'TU_TOKEN'
bot = telebot.TeleBot(TOKEN)

# Lista de cartas y reglas
cards = [
    ['Muldrotha', 'https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=573046&type=card'],
    ['Underworld Cerberus', 'https://i.ebayimg.com/images/g/LqEAAOSw75JdBQ2o/s-l1200.jpg'],
    ['Sol Ring', 'https://cards.scryfall.io/png/front/7/4/7454e0cc-98c2-48a1-b2c9-49908d2aedcc.png?1690002851'],
]

rules = [
    ['Regla 1', 'Leer la carta, explica la carta'],
    ['Regla 2', 'El jugador pierde cuando su vida llega a 0'],
    ['Regla 3', 'En duelo, la vida base es 20. \n En rueda, la vida base es 40'],
]
# Creacion de comandos simples como `/start` y `/help`
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola! Soy tu BOT de Magic The Gathering. Puedo ayudarte a buscar cartas, reglas y mucho más. Usa el comando /help para ver todas las opciones.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Estos son los comandos que puedes usar: \n /start - Inicia el BOT \n /help - Muestra esta ayuda \n /card - Busca una carta por su nombre \n /rule - Busca una regla por su nombre \n /random - Muestra una carta o regla aleatoria")

# Funcion random para retornar dos botones para seleccionar carta o regla
@bot.message_handler(commands=['random'])
def send_options(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    # Creando botones
    rd_card = types.InlineKeyboardButton('Carta aleatoria', callback_data='random_card')
    rd_rule = types.InlineKeyboardButton('Regla aleatoria', callback_data='random_rule')

    # Agregando botones al markup
    markup.add(rd_card, rd_rule)

    # Enviando mensaje con botones
    bot.send_message(message.chat.id, "Elige una opción:", reply_markup=markup)

# Manejando la respuesta de los botones
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'random_card':
        bot.answer_callback_query(call.id, "Mostrando carta aleatoria...")
        random_card = random.choice(cards)
        # bot.send_message(call.message.chat.id, f"{random_card[0]}")
        bot.send_photo(chat_id=call.message.chat.id, photo=random_card[1], caption=random_card[0])
    elif call.data == 'random_rule':
        bot.answer_callback_query(call.id, "Mostrando regla aleatoria...")
        random_rule = random.choice(rules)
        bot.send_message(call.message.chat.id, f"{random_rule[0]}: {random_rule[1]}")

# Buscar carta por nombre
@bot.message_handler(commands=['card'])
def search_card(message):
    card_name = message.text.split()[1:]
    card_name = ' '.join(card_name).lower()

    for card in cards:
        if card[0].lower() == card_name:
            bot.send_photo(chat_id=message.chat.id, photo=card[1], caption=f"Carta encontrada: {card[0]}")
            return   
    bot.send_message(chat_id=message.chat.id, text="Carta no encontrada, verifica que escribiste bien el nombre.")


if __name__ == "__main__":
    print("BOT iniciado correctamente.")
    bot.polling(none_stop=True)
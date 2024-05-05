import telebot
import random
from telebot import types
import cards

# Conexion con nuestro BOT
TOKEN = '7183428167:AAGV1vsM6EykluJGQP3a0mXGGORqcideY0E'
bot = telebot.TeleBot(TOKEN)

# Creacion de comandos simples como `/start` y `/help`
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola! Soy tu BOT de Pokemon. Puedo ayudarte a buscar pokemones y mucho más. Usa el comando /help para ver todas las opciones.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Estos son los comandos que puedes usar: \n /start - Inicia el BOT \n /help - Muestra esta ayuda \n /pokemon - Busca un pokemon por su nombre \n /pokemons - Muestra todos los pokemones \n /reglas - Muestra las reglas para una batalla Pokémon \n /batalla - Inicia una batalla Pokémon \n")

@bot.message_handler(commands=['reglas'])
def send_rules(message):
    rules = """
    Reglas para una batalla Pokémon:

    - Normal: débil frente a Lucha.
    - Fuego: débil frente a Agua, Tierra, Roca.
    - Agua: débil frente a Planta, Eléctrico.
    - Planta: débil frente a Fuego, Hielo, Veneno, Volador, Bicho.
    - Eléctrico: débil frente a Tierra.
    - Hielo: débil frente a Fuego, Lucha, Roca, Acero.

    Si deseas realizar una batalla, usa el comando /batalla seguido de los nombres de los Pokémon. Por ejemplo: /batalla pikachu ivysaur

    Si quieres ver la lista de Pokémon para la batalla, usa el comando /pokemons
    """
    bot.reply_to(message, rules)

# Funcion para mostrar todos los pokemones
@bot.message_handler(commands=['pokemons'])
def send_pokemons(message):
    cards.send_pokemons(bot, message)  

# Buscar pokemon por nombre
@bot.message_handler(commands=['pokemon'])
def search_pokemon(message):
    cards.search_pokemon(bot, message) 

    # Iniciar una batalla entre dos Pokémon
@bot.message_handler(commands=['batalla'])
def handle_battle_command(message):
    cards.start_battle(bot, message)  

if __name__ == "__main__":
    print("BOT iniciado correctamente.")
    bot.polling(none_stop=True)
import telebot
import random
from telebot import types

# Conexion con nuestro BOT
TOKEN = 'TU_TOKEN'
bot = telebot.TeleBot(TOKEN)

# Lista de cartas en el mazo de Muldrotha
# cards = [
#     ['Muldrotha, the Gravetide', 'https://product-images.tcgplayer.com/162139.jpg'],
#     ['Eternal Witness', 'https://product-images.tcgplayer.com/fit-in/437x437/179483.jpg'],
#     ['Sakura-Tribe Elder', 'https://product-images.tcgplayer.com/fit-in/437x437/108028.jpg'],
#     ['Demonic Tutor', 'https://product-images.tcgplayer.com/fit-in/437x437/504566.jpg'],
#     ['Cyclonic Rift', 'https://product-images.tcgplayer.com/fit-in/437x437/530800.jpg'],
#     ['Pernicious Deed', 'https://product-images.tcgplayer.com/fit-in/437x437/161726.jpg'],
#     ['Sol Ring'], 'https://product-images.tcgplayer.com/fit-in/437x437/122862.jpg',
#     ['Command Tower', 'https://product-images.tcgplayer.com/fit-in/437x437/247533.jpg'],
#     ['Strip Mine', 'https://product-images.tcgplayer.com/fit-in/437x437/32786.jpg'],
#     ['Mystic Remora', 'https://product-images.tcgplayer.com/fit-in/437x437/4815.jpg'],
#     ['Phyrexian Arena', 'https://product-images.tcgplayer.com/fit-in/437x437/535779.jpg'],
#     ['Life from the Loam', 'https://product-images.tcgplayer.com/fit-in/437x437/205249.jpg'],
#     ['Rhystic Study', 'https://product-images.tcgplayer.com/fit-in/437x437/509518.jpg'],
#     ['Counterspell', 'https://product-images.tcgplayer.com/fit-in/437x437/93772.jpg'],
#     ['Animate Dead', 'https://product-images.tcgplayer.com/fit-in/437x437/57244.jpg'],
#     ['Entomb', 'https://product-images.tcgplayer.com/fit-in/437x437/118430.jpg'],
#     ['Victimize', 'https://product-images.tcgplayer.com/fit-in/437x437/108063.jpg'],
#     ['Animate Dead'],
#     ['Buried Alive'],
#     ['Mulldrifter'],
#     ['Sylvan Library'],
#     ['Eternal Witness'],
#     ['Rampant Growth'],
#     ['Nature\'s Lore'],
#     ['Kodama\'s Reach'],
#     ['Cultivate'],
#     ['Growth Spiral'],
#     ['Ponder'],
#     ['Preordain'],
#     ['Brainstorm'],
#     ['Narset, Parter of Veils'],
#     ['Windfall'],
#     ['Cyclonic Rift'],
#     ['Reality Shift'],
#     ['Assassin\'s Trophy'],
#     ['Abrupt Decay'],
#     ['Putrefy'],
#     ['Toxic Deluge'],
#     ['Nature\'s Claim'],
#     ['Seal of Primordium'],
#     ['Lotus Petal'],
#     ['Mind Stone'],
#     ['Talisman of Dominance'],
#     ['Talisman of Resilience'],
#     ['Talisman of Curiosity'],
#     ['Commander\'s Sphere'],
#     ['Dimir Signet'],
#     ['Simic Signet'],
#     ['Golgari Signet'],
#     ['Fellwar Stone'],
#     ['Gilded Lotus'],
#     ['Ashiok, Dream Render'],
#     ['Jace, Wielder of Mysteries'],
#     ['Kiora, Behemoth Beckoner'],
#     ['Nissa, Vital Force'],
#     ['Nissa, Steward of Elements'],
#     ['Liliana, Death\'s Majesty'],
#     ['Liliana, Waker of the Dead'],
#     ['Liliana, Dreadhorde General'],
#     ['Plaguecrafter'],
#     ['Ravenous Chupacabra'],
#     ['Noxious Gearhulk'],
#     ['Glen Elendra Archmage'],
#     ['Hostage Taker'],
#     ['Mulldrifter'],
#     ['Golgari Grave-Troll'],
#     ['Sheoldred, Whispering One'],
#     ['Tireless Tracker'],
#     ['Rampaging Baloths'],
#     ['Baleful Strix'],
#     ['Coiling Oracle'],
#     ['Sakura-Tribe Elder'],
#     ['Wood Elves'],
#     ['Farhaven Elf'],
#     ['Gilded Goose'],
#     ['Birds of Paradise'],
#     ['Deathrite Shaman'],
#     ['Satyr Wayfinder'],
#     ['Stitcher\'s Supplier'],
#     ['Glowspore Shaman'],
#     ['Grisly Salvage'],
#     ['Mystic Remora'],
#     ['Nihil Spellbomb'],
#     ['Relic of Progenitus'],
#     ['Executioner\'s Capsule'],
#     ['Spore Frog'],
#     ['Golgari Charm'],
#     ['Seal of Primordium'],
#     ['Sylvan Safekeeper'],
#     ['Nihil Spellbomb'],
#     ['Relic of Progenitus'],
#     ['Executioner\'s Capsule'],
#     ['Spore Frog'],
#     ['Golgari Charm'],
#     ['Pernicious Deed'],
#     ['Nevinyrral\'s Disk'],
#     ['Perpetual Timepiece'],
#     ['Expedition Map'],
#     ['Nihil Spellbomb'],
#     ['Relic of Progenitus']
# ]

cards = [
    # Criaturas (33)
    ['* Birds of Paradise', 'https://product-images.tcgplayer.com/fit-in/437x437/499510.jpg'],
    ['* Llanowar Elves', 'https://product-images.tcgplayer.com/fit-in/437x437/456661.jpg'],
    ['* Nature\'s Lore', 'https://product-images.tcgplayer.com/fit-in/437x437/457135.jpg'],
    ['* Sylvan Library', 'https://product-images.tcgplayer.com/fit-in/437x437/221308.jpg'],
    ['* Farseek', 'https://product-images.tcgplayer.com/fit-in/437x437/519548.jpg'],
    ['* Rampant Growth', 'https://product-images.tcgplayer.com/fit-in/437x437/276283.jpg'],
    ['* Cultivate', 'https://product-images.tcgplayer.com/fit-in/437x437/48120.jpg'],
    ['* Animate Dead', 'https://product-images.tcgplayer.com/fit-in/437x437/57244.jpg'],
    ['* Living Death', 'https://product-images.tcgplayer.com/fit-in/437x437/499609.jpg'],
    ['* Reanimate', 'https://product-images.tcgplayer.com/fit-in/437x437/179471.jpg'],
    ['* Phyrexian Reclamation', 'https://product-images.tcgplayer.com/fit-in/437x437/216460.jpg'],
    ['* Eternal Witness', 'https://product-images.tcgplayer.com/fit-in/437x437/507278.jpg'],
    ['* Karmic Guide', 'https://product-images.tcgplayer.com/fit-in/437x437/247349.jpg'],
    ['* Sakura-Tribe Elder', 'https://product-images.tcgplayer.com/fit-in/437x437/269613.jpg'],
    ['* Spore Frog', 'https://product-images.tcgplayer.com/fit-in/437x437/7378.jpg'],
    ['* Plaguecrafter', 'https://product-images.tcgplayer.com/fit-in/437x437/531202.jpg'],
    ['* Scavenging Ooze', 'https://product-images.tcgplayer.com/fit-in/437x437/478590.jpg'],
    ['* Eternal Scourge', 'https://product-images.tcgplayer.com/fit-in/437x437/120731.jpg'],
    ['* Yarok, the Desecrated', 'https://product-images.tcgplayer.com/fit-in/437x437/491433.jpg'],
    ['* Muldrotha, the Gravetide', 'https://product-images.tcgplayer.com/fit-in/437x437/222357.jpg'],
    ['* Tireless Tracker', 'https://product-images.tcgplayer.com/fit-in/437x437/116913.jpg'],
    ['* Grim Haruspex', 'https://product-images.tcgplayer.com/fit-in/437x437/93158.jpg'],
    ['* Mulldrifter', 'https://product-images.tcgplayer.com/fit-in/437x437/535745.jpg'],
    ['* Rhystic Study', 'https://product-images.tcgplayer.com/fit-in/437x437/509518.jpg'],
    ['* Necromancer\'s Stockpile', 'https://product-images.tcgplayer.com/fit-in/437x437/91108.jpg'],
    ['* Oracle of Mul Daya', 'https://product-images.tcgplayer.com/fit-in/437x437/33387.jpg'],
    ['* Ugin, the Spirit Dragon', 'https://product-images.tcgplayer.com/fit-in/437x437/489674.jpg'],
    ['* Old Stickfingers', 'https://product-images.tcgplayer.com/fit-in/437x437/255844.jpg'],
    ['* Merfolk Looter', 'https://product-images.tcgplayer.com/fit-in/437x437/47693.jpg'],

    # Hechizos (34)
    ['* Swords to Plowshares', 'https://product-images.tcgplayer.com/fit-in/437x437/449580.jpg'],
    ['* Path to Exile', 'https://product-images.tcgplayer.com/fit-in/437x437/520163.jpg'],
    ['* Anguished Unmaking', 'https://product-images.tcgplayer.com/fit-in/437x437/115262.jpg'],
    ['* Assassin\'s Trophy', 'https://product-images.tcgplayer.com/fit-in/437x437/175575.jpg'],
    ['* Beast Within', 'https://product-images.tcgplayer.com/fit-in/437x437/478579.jpg'],
    ['* Maelstrom Pulse', 'https://product-images.tcgplayer.com/fit-in/437x437/179506.jpg'],
    ['* Damnation', 'https://product-images.tcgplayer.com/fit-in/437x437/97081.jpg'],
    ['* Pernicious Deed', 'https://product-images.tcgplayer.com/fit-in/437x437/38264.jpg'],
    ['* Transmute Artifact', 'https://product-images.tcgplayer.com/fit-in/437x437/3330.jpg'],
    ['* Restock', 'https://product-images.tcgplayer.com/fit-in/437x437/90981.jpg'],
    ['* Buried Alive', 'https://product-images.tcgplayer.com/fit-in/437x437/180895.jpg'],
    ['* Imperial Seal', 'https://product-images.tcgplayer.com/fit-in/437x437/477.jpg'],
    ['* Demonic Tutor', 'https://product-images.tcgplayer.com/fit-in/437x437/38238.jpg'],
    ['* Vampiric Tutor', 'https://product-images.tcgplayer.com/fit-in/437x437/226134.jpg'],
    ['* Mystical Tutor', 'https://product-images.tcgplayer.com/fit-in/437x437/457199.jpg'],
    ['* Worldly Tutor', 'https://product-images.tcgplayer.com/fit-in/437x437/457269.jpg'],
    ['* Thoughtseize', 'https://product-images.tcgplayer.com/fit-in/437x437/541262.jpg'],
    ['* Duress', 'https://product-images.tcgplayer.com/fit-in/437x437/215662.jpg'],
    ['* Inquisition of Kozilek', 'https://product-images.tcgplayer.com/fit-in/437x437/456582.jpg'],
    ['* Hymn to Tourach', 'https://product-images.tcgplayer.com/fit-in/437x437/284368.jpg'],
    ['* Counterspell', 'https://product-images.tcgplayer.com/fit-in/437x437/93772.jpg'],
    ['* Mana Drain', 'https://product-images.tcgplayer.com/fit-in/437x437/3951.jpg'],
    ['* Force of Will', 'https://product-images.tcgplayer.com/fit-in/437x437/4146.jpg'],
    ['* Swan Song', 'https://product-images.tcgplayer.com/fit-in/437x437/214903.jpg'],
    ['* Brainstorm', 'https://product-images.tcgplayer.com/fit-in/437x437/203683.jpg'],
    ['* Ponder', 'https://product-images.tcgplayer.com/fit-in/437x437/171481.jpg'],
    ['* Preordain', 'https://product-images.tcgplayer.com/fit-in/437x437/519514.jpg'],
    ['* Fact or Fiction', 'https://product-images.tcgplayer.com/fit-in/437x437/259209.jpg'],
    ['* Negate', 'https://product-images.tcgplayer.com/fit-in/437x437/35403.jpg'],
    ['* Crop Rotation', 'https://product-images.tcgplayer.com/fit-in/437x437/218444.jpg'],
    ['* Land Tax', 'https://product-images.tcgplayer.com/fit-in/437x437/167780.jpg'],
    ['* Exploration', 'https://product-images.tcgplayer.com/fit-in/437x437/218291.jpg'],

    # Artefactos (15)
    ['* Mana Crypt', 'https://product-images.tcgplayer.com/fit-in/437x437/57646.jpg'],
    ['* Mox Sapphire', 'https://product-images.tcgplayer.com/fit-in/437x437/9147.jpg'],
    ['* Mox Emerald', 'https://product-images.tcgplayer.com/fit-in/437x437/8841.jpg'],
    ['* Mox Jet', 'https://product-images.tcgplayer.com/fit-in/437x437/8842.jpg'],
    ['* Mindslaver', 'https://product-images.tcgplayer.com/fit-in/437x437/11324.jpg'],
    ['* Black Lotus', 'https://product-images.tcgplayer.com/fit-in/437x437/1042.jpg'],
    ['* Chromatic Sphere', 'https://product-images.tcgplayer.com/fit-in/437x437/216112.jpg'],
    ['* Thought Vessel', 'https://product-images.tcgplayer.com/fit-in/437x437/519283.jpg'],
    ['* Skullclamp', 'https://product-images.tcgplayer.com/fit-in/437x437/108102.jpg'],
    ['* Sensei\'s Divining Top', 'https://product-images.tcgplayer.com/fit-in/437x437/276270.jpg'],
    ['* Winter Orb', 'https://product-images.tcgplayer.com/fit-in/437x437/2449.jpg'],
    ['* Thorn of Amethyst', 'https://product-images.tcgplayer.com/fit-in/437x437/15653.jpg'],
    ['* Commander\'s Sphere', 'https://product-images.tcgplayer.com/fit-in/437x437/499563.jpg'],
    ['* Sol Ring', 'https://product-images.tcgplayer.com/fit-in/437x437/519305.jpg'],
    ['* Lantern of Insight', 'https://product-images.tcgplayer.com/fit-in/437x437/210388.jpg'],
    ['* The Underworld Cookbook', 'https://product-images.tcgplayer.com/fit-in/437x437/239734.jpg'],

    # Tierras (18)
    ['* Misty Rainforest', 'https://product-images.tcgplayer.com/fit-in/437x437/33372.jpg'],
    ['* Verdant Catacombs', 'https://product-images.tcgplayer.com/fit-in/437x437/210711.jpg'],
    ['* Polluted Delta', 'https://product-images.tcgplayer.com/fit-in/437x437/221807.jpg'],
    ['* Island', 'https://product-images.tcgplayer.com/fit-in/437x437/151825.jpg'],
    ['* Forest', 'https://product-images.tcgplayer.com/fit-in/437x437/151828.jpg'],
    ['* Swamp', 'https://product-images.tcgplayer.com/fit-in/437x437/filters:quality(1)/151826.jpg'],
    ['* Myriad Landscape', 'https://product-images.tcgplayer.com/fit-in/437x437/539886.jpg'],
    ['* Tocasia\'s Dig Site', 'https://product-images.tcgplayer.com/fit-in/437x437/535692.jpg'],
    ['* Underground Sea', 'https://product-images.tcgplayer.com/fit-in/437x437/9240.jpg'],
    ['* Twilight Mire', 'https://product-images.tcgplayer.com/fit-in/437x437/110739.jpg'],
    ['* Bojuka Bog', 'https://product-images.tcgplayer.com/fit-in/437x437/545383.jpg'],
    ['* Cabal Coffers', 'https://product-images.tcgplayer.com/fit-in/437x437/38075.jpg'],
    ['* Urborg, Tomb of Yawgmoth', 'https://product-images.tcgplayer.com/fit-in/437x437/91106.jpg'],
    ['* Thespian\'s Stage', 'https://product-images.tcgplayer.com/fit-in/437x437/218436.jpg'],
    ['* Forest', 'https://product-images.tcgplayer.com/fit-in/437x437/206026.jpg'],
]

# Lista de reglas del juego
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

# Funcion para mostrar todas las cartas del mazo
@bot.message_handler(commands=['cards'])
def send_cards(message):
    try:
        bot.send_message(chat_id=message.chat.id, text='Las 100 mejores cartas para jugar con Muldrotha:')
        for card in cards:
            bot.send_photo(chat_id=message.chat.id, photo=card[1], caption=card[0])
            #bot.send_message(chat_id=message.chat.id, text=card)
    except Exception as e:
        print(f"Error: {e}")
        bot.send_message(chat_id=message.chat.id, text="Ha ocurrido un error ejecutando su petición.")

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
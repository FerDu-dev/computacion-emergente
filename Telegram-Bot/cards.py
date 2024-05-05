import requests

# Funcion para mostrar todos los pokemones
def send_pokemons(bot, message):
    try:
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=50')
        data = response.json()

        for pokemon in data['results']:
            pokemon_response = requests.get(pokemon['url'])
            pokemon_data = pokemon_response.json()

            # Enviar la foto del Pokemon
            bot.send_photo(chat_id=message.chat.id, photo=pokemon_data['sprites']['front_default'])

            # Formatear las habilidades
            abilities = ', '.join([f"{ability['ability']['name']}({ability['slot']})" for ability in pokemon_data['abilities']])

            # Crear y enviar el mensaje con los datos
            message_text = f"Datos {pokemon_data['name'].capitalize()}:\n"
            message_text += f"Pokedex: {pokemon_data['id']}\n"
            message_text += f"Habilidades: {abilities}\n"
            message_text += f"Fuerza: {pokemon_data['base_experience']}"

            bot.send_message(chat_id=message.chat.id, text=message_text)

    except Exception as e:
        print(f"Error: {e}")
        bot.send_message(chat_id=message.chat.id, text="Error al obtener la lista de pokemones.")

# Buscar pokemon por nombre
def search_pokemon(bot, message):
    pokemon_name = message.text.split()[1:]
    pokemon_name = ' '.join(pokemon_name).lower()

    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
        data = response.json()

        # Enviar la foto del Pokemon
        bot.send_photo(chat_id=message.chat.id, photo=data['sprites']['front_default'])

        # Formatear los movimientos
        moves = ', '.join([move['move']['name'] for move in data['moves'][:4]])

        # Formatear las estadísticas
        stats = '\n'.join([f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}" for stat in data['stats']])

        # Formatear los tipos
        types = ', '.join([type['type']['name'] for type in data['types']])

        # Crear y enviar el mensaje con los datos
        message_text = f"Datos de {data['name'].capitalize()}:\n"
        message_text += f"Pokedex: {data['id']}\n"
        message_text += f"Tipo: {types}\n"
        message_text += f"Movimientos: {moves}\n"
        message_text += f"Estadísticas:\n{stats}"

        bot.send_message(chat_id=message.chat.id, text=message_text)

    except Exception as e:
        print(f"Error: {e}")
        bot.send_message(chat_id=message.chat.id, text="Pokemon no encontrado, verifica que escribiste bien el nombre.")

# Iniciar una batalla Pokémon
def start_battle(bot, message):
    pokemon_names = message.text.split()[1:]

    if len(pokemon_names) != 2:
        bot.reply_to(message, "Debes proporcionar exactamente dos nombres de Pokémon para iniciar una batalla. Por ejemplo: /batalla pikachu ivysaur")
        return

    try:
        # Obtener los datos de los Pokémon
        pokemon_data = []
        for name in pokemon_names:
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
            data = response.json()
            pokemon_data.append(data)

        # Comparar las estadísticas de los Pokémon
        hp_diff = pokemon_data[0]['stats'][0]['base_stat'] - pokemon_data[1]['stats'][0]['base_stat']
        attack_diff = pokemon_data[0]['stats'][1]['base_stat'] - pokemon_data[1]['stats'][1]['base_stat']
        defense_diff = pokemon_data[0]['stats'][2]['base_stat'] - pokemon_data[1]['stats'][2]['base_stat']

        # Determinar el ganador y la razón
        reasons = []
        if hp_diff > 0:
            reasons.append("HP")
        if attack_diff > 0:
            reasons.append("Ataque")
        if defense_diff > 0:
            reasons.append("Defensa")

        if hp_diff + attack_diff + defense_diff > 0:
            winner = pokemon_data[0]['name']
        else:
            winner = pokemon_data[1]['name']

        reason_text = ', '.join(reasons) if reasons else "Tipo"
        bot.send_photo(chat_id=message.chat.id, photo=pokemon_data[0]['sprites']['front_default'])
        bot.send_message(chat_id=message.chat.id, text=f"El ganador de la batalla es {winner.capitalize()} debido a su superior {reason_text}!")

    except Exception as e:
        print(f"Error: {e}")
        bot.send_message(chat_id=message.chat.id, text="Error al iniciar la batalla. Asegúrate de que los nombres de los Pokémon son correctos.")
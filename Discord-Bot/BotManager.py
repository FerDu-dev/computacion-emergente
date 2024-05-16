import configs.DefaultConfig as defaultConfig
import utils.DiscordUtil as discordUtil

import asyncio
import discord
from discord.ext import commands
from cogs.GeminiCog import GeminiAgent

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
  print('Bot iniciado correctamente...')

@bot.event
async def on_member_join(member):
  print('Nuevo miembro en el servidor...')
  guild = member.guild
  guildname = guild.name
  dmchannerl = await member.create_dm()
  await dmchannerl.sned(f'Bienvenido a {guildname}, {member.name}! Espero que disfrutes tu estancia en el servidor.')

@bot.command(aliases = ["about", "info"])
async def help(ctx):
  MyEmbed = discord.Embed(title="Comandos",
                          description="Lista de comandos disponibles. Cuando interactues por privado no es necesario usar los comandos, puedes tener una conversacion normal.",
                          color=discord.Colour.blue())
  MyEmbed.set_thumbnail(url="https://i.redd.it/llkxvsttlptb1.jpg")
  MyEmbed.add_field(name="!query", value="Preguntale al bot de Gemini lo que desees. Por favor, recuerda usar signo de pregunta (Este -> ?).", inline=False)
  MyEmbed.add_field(name="!pm", value="Envia un mensaje privado a Gemini.", inline=False)
  await ctx.send(embed=MyEmbed)

@bot.command()
@commands.check(discordUtil.is_me)
async def unloadGemini(ctx):
  await bot.remove_cog('GeminiAgent')

@bot.command()
@commands.check(discordUtil.is_me)
async def reloadGemini(ctx):
  await bot.add_cog(GeminiAgent(bot))

async def start_cogs():
  await bot.add_cog(GeminiAgent(bot))

asyncio.run(start_cogs())
bot.run(defaultConfig.DISCORD_SDK)

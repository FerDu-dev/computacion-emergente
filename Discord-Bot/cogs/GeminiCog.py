import configs.DefaultConfig as defaultConfig
import utils.DiscordUtil as discordUtil
from discord.ext import commands
import google.generativeai as genai

genai.configure(api_key=defaultConfig.GEMINI_SDK)
DISCORD_MAX_MESSAGE_LENGTH = 2000
PLEASE_TRY_AGAIN_ERROR_MESSAGE = "No entiendo tu pregunta, por favor, intenta de nuevo..."

class GeminiAgent(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    self.model = genai.GenerativeModel('gemini-pro')

  @commands.Cog.listener()
  async def on_message(self, msg):
    try:
      if msg.content == 'ping gemini-agent':
        await msg.channel.send('El Agente Gemini esta listo para responder tus preguntas...')
      elif 'Direct Message' in str(msg.channel) and not msg.author.bot:
        response = self.gemini_generate_content(msg.content)
        dmchannel = await msg.author.create_dm()
        await dmchannel.send(response.text)
    except Exception as e:
      return PLEASE_TRY_AGAIN_ERROR_MESSAGE + str(e)

  @commands.command()
  async def ask(self, ctx, question):
    try:
      response = self.gemini_generate_content(question)
      await ctx.send(response.text)
    except Exception as e:
      await ctx.send(PLEASE_TRY_AGAIN_ERROR_MESSAGE + str(e))
  
  @commands.command()
  async def dm(self, ctx):
    # Revisa si el usuario puede recibir mensajes de miembros del servidor
    if not ctx.author.dm_channel:
      try:
        dmchannel = await ctx.author.create_dm()
        await dmchannel.send('Hola! Soy Gemini, el asistente virtual de Google. ¿En qué puedo ayudarte?')
      except:
        await ctx.send("No es posible enviarte mensajes privados :(. Por favor habilita los mensajes de miembros del servidor para interactuar por privado.")
        return
    
  def gemini_generate_content(self, content):
    try:
      return self.model.generate_content(content)
    except Exception as e:
      return PLEASE_TRY_AGAIN_ERROR_MESSAGE + str(e)
from dotenv import load_dotenv
import discord
import os

from services.ChatGPTService import ChatGpt

load_dotenv()
CHAT_GPT_DISCORD_TOKEN = str(os.environ.get("CHAT_GPT_DISCORD_TOKEN"))

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    command = message.content.split(" ")[0]
    if message.author == client.user:
        return
    
    if command == "/chat":
        question = 'Who was the president of the United States in 1970?'
        chatService = ChatGpt()
        response = chatService.getMessage(question)
        await message.channel.send(response)

client.run(CHAT_GPT_DISCORD_TOKEN)
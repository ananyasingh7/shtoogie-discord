from dotenv import load_dotenv
from services.WeatherService import WeatherService
import discord
import os

load_dotenv()
WEATHER_SERVICE_API_TOKEN = os.environ.get("WEATHER_SERVICE_API_TOKEN")
WEATHER_DISCORD_TOKEN = str(os.environ.get("WEATHER_DISCORD_TOKEN"))

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/weather'):
        weather_service = WeatherService(WEATHER_SERVICE_API_TOKEN)
        if len(message.content.split(" ")) >= 3:
            city = " ".join(message.content.split(" ")[1:])
            id = weather_service.get_location_id(city)
            content = weather_service.get_weather_by_id(id)
            await message.channel.send(content)
        elif len(message.content.split(" ")) >= 2:
            city = message.content.split(" ")[1]
            id = weather_service.get_location_id(city)
            content = weather_service.get_weather_by_id(id)
            await message.channel.send(content)
        else:
            id = weather_service.get_location_id('cedar grove')
            content = weather_service.get_weather_by_id(id)
            await message.channel.send(content)

client.run(WEATHER_DISCORD_TOKEN)

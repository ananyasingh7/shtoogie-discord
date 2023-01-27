import discord

from services.StockService import StockService
import json

from dotenv import load_dotenv
import os
load_dotenv()

STOCK_SERVICE_API_TOKEN = os.environ.get("STOCK_SERVICE_API_TOKEN")
STOCK_DISCORD_TOKEN = str(os.environ.get("STOCK_DISCORD_TOKEN"))

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    stockService = StockService(STOCK_SERVICE_API_TOKEN)
    command = message.content.split(" ")[0]

    if message.author == client.user:
        return

    if command == "/stock":
        stockTicker = message.content.split(" ")[1]
        price = stockService.get_stock_info(stockTicker, False)
        await message.channel.send(f"The current price of ${stockTicker} is ${price}.")

    if command == '/stockInfo':
        stockTicker = message.content.split(" ")[1]
        price = stockService.get_stock_info(stockTicker, True)
        formattedJsonOutput = json.dumps(price, indent=2)
        await message.channel.send(f"```{formattedJsonOutput}```")

client.run(STOCK_DISCORD_TOKEN)
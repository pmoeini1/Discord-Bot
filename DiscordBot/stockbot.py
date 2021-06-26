import discord
import os
from dotenv import load_dotenv
from urllib.request import urlopen


# generate WSJ stock page url
def scrapeTarget(ticker):
    url = "https://www.wsj.com/market-data/quotes/" + ticker + "/research-ratings"
    return url

# client constructor
client = discord.Client()

# print once ready
@client.event
async def on_ready():
    print("{0.user}".format(client))


@client.event
async def on_message(message):
    # if link is not valid, send warning url
    if message.author == client.user:
        if (len(message.embeds)==0 and not message.content == "Valid url not found, please search externally"):
            await message.channel.send("Valid url not found, please search externally")
    # send WSJ url for desired stock ticker
    if message.content.startswith('$target') or message.content.startswith('!target'):
        ticker = message.content.split("target ")[1]
        ticker = ticker.split(" ")[0]
        # scraping method here
        await message.channel.send(scrapeTarget(ticker))

# get bot token and run bot
load_dotenv()
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)

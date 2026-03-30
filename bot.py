import requests
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
from discord.ui import View, Select, Modal, TextInput

from keep_alive import keepalive

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

keepalive()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)


def getmeowfacts():
    url = "https://meowfacts.herokuapp.com/"

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        acdata = data["data"]
        acdata = str(acdata)
        acdata = acdata.replace("[", "").replace("]", "").replace("'", "")
        return(acdata)
    else:
        return(f"Something went wrong: Error Code: {response.status_code}")



@bot.event
async def on_ready():
    print(f"online")





@bot.tree.command(name="catfacts", description="Roll a cat fact")
async def catfacts(interaction):
    await interaction.response.send_message(getmeowfacts())





bot.run(token)

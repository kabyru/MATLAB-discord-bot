# bot.py
import os

import discord
from dotenv import load_dotenv
import subprocess

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "compute" in message.content:
        cleanedOutput = str(message.content)[7:]
        
        command = "matlab -batch \"" + cleanedOutput + "\", shell=True"
        output = subprocess.check_output(command)
        cleanedOutput = str(output.decode('utf-8')).replace('\r','').replace('\n','')
        print(cleanedOutput)

        formattedOutput = "```" + cleanedOutput + "```"
    
        await message.channel.send(formattedOutput)

client.run(TOKEN)
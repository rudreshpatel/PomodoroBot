import os
import discord
import datetime
from dotenv import load_dotenv
import time

starttime = datetime.datetime.now()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
RUDRESH = os.getenv('RUDRESH_ID')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        print(f'{client.user} is connected to {guild.name} (id: {guild.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f'Name: {message.author.name}, ID: {message.author.id}')
    if str(message.author.id) == RUDRESH:
        if "!study" == message.content:
            timelength = 0
            await message.channel.send('Now, please input a time using !studytime (int):')
        if message.content.startswith("!studytime "):
            timelength = int(message.content[11:])
            starttime = datetime.datetime.now()
            pingtime = starttime + datetime.timedelta(seconds=timelength)
            await message.reply(f'Start time: {starttime.strftime("%b. %d - %H:%M:%S")}, Ping time: {pingtime.strftime("%b. %d - %H:%M:%S")}')
            time.sleep(timelength)
            await message.channel.send("Your study period has concluded. Please use !break to start your break")

        if "!break" == message.content:
            breaktime = 0
            await message.channel.send('Now, please input a time using !breaktime (int):')
        if message.content.startswith("!breaktime "):
            breaktime = int(message.content[11:])
            breakstart = datetime.datetime.now()
            pingbreaktime = breakstart + datetime.timedelta(seconds=breaktime)
            await message.reply(f'Start time: {breakstart.strftime("%b. %d - %H:%M:%S")}, Ping time: {pingbreaktime.strftime("%b. %d - %H:%M:%S")}')
            time.sleep(breaktime)
            await message.channel.send("Your break period has concluded. Please use !study to start your studytime")


client.run(TOKEN)
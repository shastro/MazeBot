'''
Main Script for running the bot with discord.py

@bug none

@todo Implement Better Command Parsing, as well as more commands
Implement help
'''
import discord
import subprocess
import os
import re


# https://discordapp.com/api/oauth2/authorize?client_id=525510742770843678&permissions=100416&scope=bot
# BOT URL, Replace client_id and permissions with your own

# Import "Secret" data
# --NOTE--
# secrets.txt should contain only two lines, the first being the bot token, and the second being the client secret
secrets = open('secrets.txt', 'r')
BOT_TOKEN = secrets.readline()
CLIENT_SECRET = secrets.readline()
secrets.close()

# Stripping Trailing Newline char from BOT_TOKEN
BOT_TOKEN = BOT_TOKEN.rstrip()

# Create Client
client = discord.Client()

# Windows Path
abs_path = os.path.abspath(r"..\..\Processing\maze_gen")

# Regex for !maze commands

mz_format = re.compile(r'^!maze\s?(\d{1,2})?')


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author.name}: {message.content}")

    if "!maze" == message.content.lower():
        await message.channel.send("Generating Maze...")
        p = subprocess.Popen(f'processing-java --sketch="{abs_path}" --run', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #out = p.stdout.read().split('\r\n')
        # print(out)
        mazefile = discord.File(rf"{abs_path}\maze.png", filename="maze.png")
        await message.channel.send(file=mazefile)

    # if "!help" == message.content.lower():

    if "!end" == message.content.lower():
        await message.channel.send("Goodbye")
        await client.close()


def evaluate_command(msg):

    mz_format = re.compile(r'^!maze\s?(\d{1,2})?')
    matches = mz_format.finditer(msg)

    for match in matches:
        print(match.group(0))


client.run(BOT_TOKEN)

'''
Main Script for running the bot with discord.py

@bug none

@todo Implement Better Command Parsing, as well as more commands
Implement !help command
Refactor conditional if !maze in msg, instead I'd like to use the regex
Implement Error Checking on match.group(1) should print an error if value not between 3 and 200
'''
import discord
import subprocess
import os
import re
import time as t


# https://discordapp.com/api/oauth2/authorize?client_id=525510742770843678&permissions=100416&scope=bot
# BOT URL, Replace client_id and permissions with your own

# Import "Secret" data
# --NOTE--
# secrets.txt should contain only two lines, the first being the bot token, and the second being the client secret
with open('secrets.txt', 'r') as secrets:
    BOT_TOKEN = secrets.readline()
    CLIENT_SECRET = secrets.readline()


# Stripping Trailing Newline char from BOT_TOKEN
BOT_TOKEN = BOT_TOKEN.rstrip()

# Create Client
client = discord.Client()

# Windows Path
abs_path = os.path.abspath(r"..\..\Processing\maze_gen")

# Regex for !maze command
mz_format = re.compile(r'^!maze\s?(-s\d{1,3})?')


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author.name}: {message.content}")

    if "!maze" in message.content.lower():
        await message.channel.send("Generating Maze...")
        await evaluate_command(message.content.lower())
        mazefile = discord.File(rf"{abs_path}\maze.png", filename="maze.png")
        await message.channel.send(file=mazefile)
        os.remove(rf"{abs_path}\maze.png")

    # if "!help" == message.content.lower(): #Todo

    if "!quit" == message.content.lower():
        await message.channel.send("Goodbye")
        await client.close()

# Handles !maze Command execution based upon msg content


async def evaluate_command(msg):

    match = mz_format.search(msg)

    if match.group(1) != None:
        p = subprocess.Popen(['processing-java', f'--sketch={abs_path}', '--run', f'{match.group(1)}'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # print(p.stdout.decode('utf-8'))
    else:
        p = subprocess.Popen(['processing-java', f'--sketch={abs_path}', '--run', f'{match.group(1)}'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # print(p.stdout.decode('utf-8'))
    p.wait()  # Wait for subprocess to finish before proceeding

client.run(BOT_TOKEN)

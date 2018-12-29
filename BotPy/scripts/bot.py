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

TIME_OUT = 10  # Timeout for command to break (seconds)

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
mz_format = re.compile(r'^!maze\s(-s=)?(\d{1,3})?\s?(-i)?')


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author.name}: {message.content}")

    if "!maze" == message.content.lower()[0:5]:
        await message.channel.send("Generating Maze...")
        await evaluate_command(message)
        # Bot Communicates with discord, and cleans up maze.png
        mazefile = discord.File(rf"{abs_path}\maze.png", filename="maze.png")
        await message.channel.send(file=mazefile)
        os.remove(rf"{abs_path}\maze.png")

    if "!help" == message.content.lower():  # Todo
        await message.channel.send("```Usage \"!maze -s=NUM -i\"\n-s=NUM defines the resolution of the maze grid, the explicit \"-s=\" is optional\n-i sets the Incomplete flag, creates a maze that does not fill every cell```")

    if "!quit" == message.content.lower():
        await message.channel.send("Goodbye")
        await client.close()

'''
Handles !maze Command execution based upon message.content

'''


async def evaluate_command(message):

    # Search Using mz_formate regex
    match = mz_format.search(message.content.lower())

    # Input Processing

    # Default Args
    s = 15  # Size
    incomplete = 0  # Incomplete flag (-i) Bool, 0 for False, 1 for True

    #(-s=) Flag
    if match != None:
        if match.group(2) != None:
            if int(match.group(2)) >= 2 and int(match.group(2)) <= 200:
                s = int(match.group(2))
            else:
                await message.channel.send("Input Error: -s=Num, Num must be between 2 and 200, using default value of 15")
        # (-i) Flag
        if match.group(3) != None:
            incomplete = 1

    # Launch Subprocess
    p = subprocess.Popen(['processing-java', f'--sketch={abs_path}', '--run', f'{s}', f'{incomplete}'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Timeout Handling
    try:
        p.wait(TIME_OUT)
    except subprocess.TimeoutExpired:
        p.kill()
        print("Subprocess Timeout, Error!")
        await message.channel.send("Internal Error: TIMEOUT, Try Again")


# Run Bot
client.run(BOT_TOKEN)

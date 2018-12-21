'''
Main Script for running the bot with discord.py
@bug
@todo
'''
import discord
import subprocess
import os


# https://discordapp.com/api/oauth2/authorize?client_id=525510742770843678&permissions=100416&scope=bot
# BOT URL, Replace client_id and permissions with your own

# Import "Secret" data
# --NOTE--
# secrets.txt should contain only two lines, the first being the bot token, and the second being the client secret
secrets = open('secrets.txt', 'r')
BOT_TOKEN = secrets.readline()
CLIENT_SECRET = str(secrets.readline())
secrets.close()

# Stripping Trailing Newline char from BOT_TOKEN
BOT_TOKEN = BOT_TOKEN.rstrip()

# Create Client
client = discord.Client()

abs_path = os.path.abspath(r"..\..\Processing\maze_gen")  # Windows Path
print(abs_path)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author.name}: {message.content}")

    if "!maze" in message.content.lower():
        await message.channel.send("Generating Maze...")
        p = subprocess.Popen(f'processing-java --sketch="{abs_path}" --run', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #out = p.stdout.read().split('\r\n')
        # print(out)
        mazefile = discord.File(rf"{abs_path}\maze.png", filename="maze.png")
        await message.channel.send(file=mazefile)

    if "!end" == message.content.lower():
        await message.channel.send("Goodbye")
        await client.close()


client.run(BOT_TOKEN)

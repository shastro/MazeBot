import discord

# https://discordapp.com/api/oauth2/authorize?client_id=525510742770843678&permissions=100416&scope=bot
# BOT URL, Replace client_id with your own

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


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author.name}: {message.content}")

    if "!maze" in message.content.lower():
        await message.channel.send("Hi")



    if "!end" == message.content.lower():
        await client.close()


client.run(BOT_TOKEN)

import discord

# https://discordapp.com/api/oauth2/authorize?client_id=525510742770843678&permissions=100416&scope=bot
# BOT URL, Replace client_id with your own

# Import "Secret" data
# --NOTE--
# secrets.txt should contain only two lines, the first being the bot token, and the second being the client secret
secrets = open('secrets.txt', 'r')
BOT_TOKEN = secrets.readline()
CLIENT_SECRET = secrets.readline()
print(BOT_TOKEN)
print(CLIENT_SECRET)

secrets.close()

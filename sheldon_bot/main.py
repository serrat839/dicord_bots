import discord
from discord.ext import commands
import logging
import sentiment

# set up client stuff
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
token = open("secret.txt", "r").read()

# set up logging
logging.basicConfig(level=logging.INFO)

# make our sentiment dict object
sentiment_dict = sentiment.make_sentiment_dict()

joel = "167458501138972672"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # testing hello
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    # testing get all members
    elif message.content.startswith("$members"):
        x = message.guild.members
        msg = "In this server, we have...\n"
        print(message.guild.members)
        for member in x:
            msg += member.name + " - "
            if len(member.roles) > 1:
                msg += member.roles[len(member.roles) - 1].name
            else:
                msg += "none :("

            msg += "\n"
            print(member.name, member.roles)
        await message.channel.send(msg)

    # bazinga
    elif message.content.startswith("$bazinga"):
        await message.channel.send(file=discord.File("images/hello_world.png"))
        # print(message.content)

    # respond to someone mentioning me
    # keep tally of number of mentions, if exceeds rate, call them out lolol
    elif "sheldon" in message.content.lower():
        result = sentiment.sentiment_analyze(message.content, sentiment_dict)
        send = ""
        if result > 0:
            send += "aww thanks I think?"
        elif result < 0:
            if str(message.author.id) == joel:
                send += "fuck off joel, ill kill you"
            else:
                send += "wow, okay smh..."
        else:
            send += "dat me, im sheldon"
        await message.channel.send(send)

client.run(token)

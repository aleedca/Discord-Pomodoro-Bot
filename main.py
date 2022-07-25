import discord

TOKEN = 'TOKEN HERE'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username} : {user_message}  ({channel})')


    if message.author == client.user:
        return

    if message.channel.name == "wanna-talk":
        if user_message.lower() == "hello":
            await message.channel.send(f'Hello {username}!')
            return


client.run(TOKEN)
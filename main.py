import discord
import datetime
import asyncio
from discord.ext import commands
bot = commands.Bot(command_prefix='!') #bot is an extension of client and it runs events the same way as client

TOKEN = 'here'

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message, titl=None, pass_context=True):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username} : {user_message}  ({channel})')

    if message.author == bot.user:
        return

    if message.channel.name == "wanna-talk":
        if user_message.lower() == "hello":
            await message.channel.send(f'Hello {username}!')
            return

        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye, ❤️ You!')
            return
    await bot.process_commands(message) #without this at the end of any on_message the commands dont work

@bot.command(help = "start your 30 sec timer", name = 'session30')
async def session30(message):
    username = str(message.author).split("#")[0]
    await message.channel.send(f'Hello {username}, Hope you are doing good, And as you selected quick 30 sec session here you go...')
    
    def check(message):
        return message.author == message.author and message.channel == message.channel
    
    try:
        msg = await bot.wait_for('message', timeout=30.0, check=check)

    except asyncio.TimeoutError:
        mention = message.author.mention
        await message.channel.send(f"Hi, {mention} hope you had a good time!")
        embed = discord.Embed(
        title="Poll", description='Good! You did it....\n So how was your session?')
        response = await message.channel.send(embed=embed)

        await response.add_reaction('👍')
        await response.add_reaction('❤️')
        await response.add_reaction('💯')
        await response.add_reaction('👎')
        return
    return

@bot.command(name = "start")
async def start(message):
    questions = [ f"Which channel should your poll be sent to?"]
    answers = []

    def check(m):
        return m.author == message.author and m.channel == message.channel

    for i in questions:
        await message.channel.send(i)

        try:
            msg = await bot.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await message.channel.send("Setup timed out, please be quicker next time!")
            return

        else:
            answers.append(msg.content)

        try:
            c_id = int(answers[0][2:-1])
        except:
            await message.channel.send(f"You didn't mention a channel properly, please format like {message.channel.mention} next time.")
            return

        channel = bot.get_channel(c_id)

        embed = discord.Embed(title="Poll", description='Fuck you i did it')
        response = await message.channel.send(embed=embed)
        await response.add_reaction('👍')
        await response.add_reaction('👎')
        return

@bot.command(help = "nonsense command")
async def ping(message):
	await message.channel.send("pong")

bot.run(TOKEN)
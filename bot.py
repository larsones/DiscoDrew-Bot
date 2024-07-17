import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
Server = os.getenv('DISCORD_SERVER')
#
#intents = discord.Intents.default()
#client = discord.Client(intents=intents)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True) #intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord !')

@bot.command(name='help')
async def getHelp(ctx):
    response = "Hi, thanks for using DiscoDrew, here are the currently available commands:\n"
    await ctx.send(response)
@bot.command(name='play')
async def getSong(ctx, args):
    #Loop through whole message to get actual string of the song name, then pass the song name and possibly artist to spotify and search if exists
    #If it does add it to the queue at the back and continue 
    #Else notify user and list the three closest matches
    return

@bot.command(name='playTube')
async def playYoutube(ctx, *args):
    voiceChannel = ctx.author.voice.channel
    if voiceChannel is None:
        await ctx.send("You are not in a voice channel for me to play music!")
        return
    
    await voiceChannel.connect()#bot.join_voice_channel(voiceChannel.channel)

 #   else:   
#        await botChannel.voice_client_move_to(voiceChannel)

"""
@bot.command(name='skip')
async def skipSong(ctx, args):
    #Create a message asking to confirm skip if ineractions yes is greater than 1/2 of the current Voice Call group pop the current song from the queue and start the play of the next song
    #   
"""
bot.run(TOKEN)
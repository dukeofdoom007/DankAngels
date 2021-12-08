import os
try:
  os.system("python3 -m poetry add discord")
  os.system("python3 -m poetry remove discord")
except:
  pass
#os.system("python3 -m poetry remove discord.py")
#os.system("pip install py-cord")
os.system("pip install --upgrade --force-reinstall py-cord")
os.system("pip install git+https://github.com/Pycord-Development/pycord@master")
import discord
from discord.ext import commands , tasks 
from datetime import datetime
import keep_alive


client = commands.Bot(command_prefix=['d!'],
                        #intents = intents,
                        case_insentive = True,
                        )

client.prefix = ['da','d!']

client.colors = {
    "WHITE": 0xFFFFFF,
    "AQUA": 0x1ABC9C,
    "GREEN": 0x2ECC71,
    "BLUE": 0x3498DB,
    "PURPLE": 0x9B59B6,
    "LUMINOUS_VIVID_PINK": 0xE91E63,
    "GOLD": 0xF1C40F,
    "ORANGE": 0xE67E22,
    "RED": 0xE74C3C,
    "NAVY": 0x34495E,
    "DARK_AQUA": 0x11806A,
    "DARK_GREEN": 0x1F8B4C,
    "DARK_BLUE": 0x206694,
    "DARK_PURPLE": 0x71368A,
    "DARK_VIVID_PINK": 0xAD1457,
    "DARK_GOLD": 0xC27C0E,
    "DARK_ORANGE": 0xA84300,
    "DARK_RED": 0x992D22,
    "DARK_NAVY": 0x2C3E50,
}
client.color_list = [c for c in client.colors.values()]
memberCount = sum([guild.member_count for guild in client.guilds])
client.startTime = datetime.now()   

def dev(ctx):
    return ctx.author.id == 755851235642572971 or ctx.author.id == 901314604779589644
  
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      client.load_extension(f'cogs.{filename[:-3]}')

@client.command(name='load')
@commands.check_any(commands.is_owner(), 
  commands.check(dev))
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  await ctx.send(f'{extension} loaded')

@client.command(name='unload')
@commands.check_any(commands.is_owner(), 
  commands.check(dev))
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  await ctx.send(f'{extension} unloaded')


  pass

@client.command(name='reload')
@commands.check_any(commands.is_owner(), 
  commands.check(dev))
async def reload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  client.load_extension(f'cogs.{extension}')
  await ctx.send(f'{extension} reloaded')

@client.event
async def on_ready():
  print(discord.__version__)

@client.event
async def on_message(message):
 
    print(message.channel.id)
    if message.channel.id == 916513770942124072 and 'd!' in message.content:
      if not message.author.id == 886179958836314132:

        await message.channel.send("No bot commands in <#916513197719171095>")
        return

my_secret = os.environ['token']
keep_alive.keep_alive()
client.run(my_secret)
import discord
from discord.ext import commands
from discord.commands import  slash_command

import contextlib
import io
import textwrap
import os
from traceback import format_exception
import sys
import random
from sys import exit
import random
import asyncio 

def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content    
def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)
def paginate(lines, chars=1500):
    size = 0
    message = []
    for line in lines:
        if len(line) + size > chars:
            yield message
            message = []
            size = 0
        message.append(line)
        size += len(line)
    yield message

class admin(commands.Cog):
  def __init__(self, client):
    self.client = client
  def dev(ctx):
    return ctx.author.id == 755851235642572971 or ctx.author.id == 901314604779589644



  @commands.command(name="eval")
  @commands.check_any(commands.is_owner(), 
  commands.check(dev))
  async def _eeval(self, ctx, *,code):
    
    code = clean_code(code)

    local_variables = {
      "discord":discord,
      "commands":commands,
      "self":self,
      "ctx":ctx,
      "channel": ctx.channel,
      "author": ctx.author,
      "guild": ctx.guild,
      "message": ctx.message,
      "os": os,
      "random": random,
      "asyncio": asyncio ,
      
    }
    
    stdout = io.StringIO()

    try:
      with contextlib.redirect_stdout(stdout):
        exec( 
          f"async def func():\n{textwrap.indent(code, '    ')}", local_variables
        )

        obj = await local_variables["func"]()
        result = f"{stdout.getvalue()}\n-- {obj}\n"
    except Exception as e:
      result = "".join(format_exception(e, e, e.__traceback__))


    if 'with open' in code and ctx.author.id != 716525960643739798 :
      return
    if 'lambda' in code:
      return 
    
    
    for message in paginate(result):
      result= ''.join(message)
      resultem = discord.Embed(title="Output", description=f"```py\n{result}```", color=random.choice(self.client.color_list))
      await ctx.send(embed=resultem)
  
  @slash_command(name="seval")
  @commands.check_any(commands.is_owner(), commands.check(dev))
  async def _eval(self, ctx, *,code):
    
    code = clean_code(code)

    local_variables = {
      "discord":discord,
      "commands":commands,
      "self":self,
      "ctx":ctx,
      "channel": ctx.channel,
      "author": ctx.author,
      "guild": ctx.guild,
      "message": ctx.message,
      "os": os,
      "random": random,
      "asyncio": asyncio ,
      
    }
    
    stdout = io.StringIO()

    try:
      with contextlib.redirect_stdout(stdout):
        exec( 
          f"async def func():\n{textwrap.indent(code, '    ')}", local_variables
        )

        obj = await local_variables["func"]()
        result = f"{stdout.getvalue()}\n-- {obj}\n"
    except Exception as e:
      result = "".join(format_exception(e, e, e.__traceback__))


    if 'with open' in code and ctx.author.id != 716525960643739798 :
      return
    if 'lambda' in code:
      return 
    
    
    for message in paginate(result):
      result= ''.join(message)
      resultem = discord.Embed(title="Output", description=f"```py\n{result}```", color=random.choice(self.client.color_list))
      await ctx.respond(embed=resultem)
  

  @slash_command(name="evale",guild_ids=[916513197719171092])
  @commands.check_any(commands.is_owner(), commands.check(dev))
  async def evyy(self, ctx, *,code):
    
    code = clean_code(code)

    local_variables = {
      "discord":discord,
      "commands":commands,
      "self":self,
      "ctx":ctx,
      "channel": ctx.channel,
      "author": ctx.author,
      "guild": ctx.guild,
      "message": ctx.message,
      "os": os,
      "random": random,
      "asyncio": asyncio ,
      
    }
    
    stdout = io.StringIO()

    try:
      with contextlib.redirect_stdout(stdout):
        exec( 
          f"async def func():\n{textwrap.indent(code, '    ')}", local_variables
        )

        obj = await local_variables["func"]()
        result = f"{stdout.getvalue()}\n-- {obj}\n"
    except Exception as e:
      result = "".join(format_exception(e, e, e.__traceback__))


    if 'with open' in code and ctx.author.id != 716525960643739798 :
      return
    if 'lambda' in code:
      return 
    
    
    
    for message in paginate(result):
      result= ''.join(message)
      resultem = discord.Embed(title="Output", description=f"```py\n{result}```", color=random.choice(self.client.color_list))
      await ctx.respond(embed=resultem)
      
def setup(client):
  client.add_cog(admin(client))
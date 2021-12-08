import discord
from discord.ext import commands
from discord.commands import  slash_command
import random

class slasht(commands.Cog):
  def __init__(self, client):
    self.client = client

  
  @commands.command()
  async def testm(self , ctx):
    
    await ctx.send('hi')

  @slash_command(guild_ids=[916513197719171092])
  async def howgay(self , ctx, args = None):
    if ctx.channel.id == 916513197719171095:
      return await ctx.respond('head over to bot channels', ephermal = True)
    k = "is"
    print(args)
    if args is None:
      harg = "You"
      k = "are"
    elif args in ctx.guild.members:
        harg = args.name
    else:
      harg = args
    
    embed = discord.Embed(description = f"{harg} {k} {random.randrange(100)}% gay")
    await ctx.respond(embed = embed)
  
  @slash_command(guild_ids=[916513197719171092])
  async def joined(self, ctx, member: discord.Member = None): 
    user = member or ctx.author
    await ctx.respond(f"{user.name} joined at {discord.utils.format_dt(user.joined_at)}")




def setup(client):
  client.add_cog(slasht(client))
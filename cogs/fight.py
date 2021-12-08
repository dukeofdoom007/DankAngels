import discord
from discord.ext import commands
from discord.commands import  slash_command
import random , asyncio
class fightbutton(discord.ui.View):
  def __init__(self):
        super().__init__()
        
        
        punch = discord.ui.Button(style=discord.ButtonStyle.green, label="punch")
        kick = discord.ui.Button(style=discord.ButtonStyle.green, label="kick")
        end = discord.ui.Button(style=discord.ButtonStyle.green, label="end")
        punch.callback = self.punch
        kick.callback = self.kick
        end.callback = self.end
        self.add_item(punch)
        self.add_item(kick)
        self.add_item(end)

        
  async def punch(self , interaction):
          for child in self.children:
                child.disabled = True
          
          
          #self.children[0].disabled = True
          
          await interaction.message.edit("punch" , view=self)
          
  async def kick(self , interaction):
          for child in self.children:
                child.disabled = True
          
          
          #self.children[0].disabled = True
          for child in self.children:
                child.disabled = True
          await interaction.message.edit("kick" , view=self)
          
  async def end(self , interaction):
          for child in self.children:
                child.disabled = True
          
          
          #self.children[0].disabled = True
          
          await interaction.message.edit("end" , view=self)
          
class fight(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command(name='fight')
  async def _fight(self , ctx, member :discord.Member = None):
    if member is None:
      return await ctx.respond("you can't just fight nobody?")
    health1 = 100
    health2 = 100
    fight = discord.Embed()
    fight.add_field(name=ctx.author.name, value =health1)
    fight.add_field(name=member.name, value =health2)
    msg = await ctx.send(embed = fight , view=fightbutton())
    #await asyncio.sleep(3)
    li = [ctx.author , member]
    winner = random.choice(li)
    if winner == ctx.author:
      win = winner
      lose = member
      health2 = 0
    else:
      win = winner
      lose = ctx.author
      health1 = 0
    fight1 = discord.Embed()
    fight1.add_field(name=ctx.author.name, value =health1)
    fight1.add_field(name=member.name, value =health2)
    #await msg.edit(f"{win.mention} has won the match" , embed = fight1)
    #while health1 >=0 or health2 >= 0:
      #pass

def setup(client):
  client.add_cog(fight(client))
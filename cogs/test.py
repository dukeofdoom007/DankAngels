import discord
from discord.ext import commands
import random

class TestView(discord.ui.View):

    def __init__(self, value):
        super().__init__()
        self.value = value
        
        scout1 = discord.ui.Button(style=discord.ButtonStyle.green, label=self.value[0])
        scout2 = discord.ui.Button(style=discord.ButtonStyle.green, label=self.value[1])
        scout3 = discord.ui.Button(style=discord.ButtonStyle.green, label=self.value[2])
        scout1.callback = self.ss
        scout2.callback = self.ss2
        scout3.callback = self.ss3
        self.add_item(scout1)
        self.add_item(scout2)
        self.add_item(scout3)

        
    async def ss(self , interaction):
          self.value = 1
          #self.children[0].disabled = True
          for child in self.children:
                child.disabled = True
          await interaction.message.edit(self.value , view=self)
          self.stop()
    async def ss2(self , interaction):
          self.value = 2
          #self.children[0].disabled = True
          for child in self.children:
                child.disabled = True
          await interaction.message.edit(self.value , view=self)
          self.stop()
    async def ss3(self , interaction):
          self.value = 3
          #self.children[0].disabled = True
          for child in self.children:
                child.disabled = True
          await interaction.message.edit(self.value , view=self)
          self.stop()
          
      
    
class test(commands.Cog):
  def __init__(self, client):
    self.client = client

  
  @commands.command()
  async def testd(self , ctx):
    rr = ['area1','area2','area3','area4','area5']
    value = []
    for i in range(3):
      value.append(random.choice(rr))
    view = TestView(value)
    await ctx.send('hi',view=view)
    
  
  

    
  @commands.Cog.listener()
  async def on_command_error(self , ctx , error):
    raise error


def setup(client):
  client.add_cog(test(client))
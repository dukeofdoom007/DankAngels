import pymongo
from pymongo import MongoClient
import os
my_secret = os.environ['password']

cluster = MongoClient(f"mongodb+srv://WES:{my_secret}@cluster0.sferx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


#client = pymongo.MongoClient("mongodb+srv://WES:<password>@cluster0.sferx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["bal"]

import discord
from discord.ext import commands
from discord.commands import  slash_command

class slht(commands.Cog):
  def __init__(self, client):
    self.client = client
  @commands.command(name = "insert")
  async def _insert(self , ctx , num :int = None):
    db = cluster["discord"]
    collection = db["bal"] 
    collection.insert_one({"_id": 0, "score": num})
#def setup(client):
  #client.add_cog(slht(client))
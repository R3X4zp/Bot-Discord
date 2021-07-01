import discord

  client =~discord.Client()
client.run("")
async def~on_ready():
print("Le Bot est Prêt.")
 @client.event~
   async def on_message (message):
     if message.content.lower() = "ping":
await message.channel.send("pong")
 default_intents = discord.Intents.default()
default_intents.membres=True
client = discord.Client(Intents=default_intents)
@client.event
async def on member_join(member):
 discord.TextChannel  = client.get_channel(853291567984541717)
await bienvenue_channel.send(content=f"Bienvenue sur le serveur){member.display_name}!"")
if message.content.startswith(""!del"):
number=int(message.content.split)()[1])
messages = await message.channel.history(limit=number + 1).flatten()
for  each_message in messages:
await each_message.delete()
from dotenv import load_dotenv 
from discord.ext import commands
load_dotenv(dotenv_path="config")
import os
  client.run(os.getenv("TOKEN"))
Class (commands.Bot)
def _inf_ (self):
super()._int_(commands_prefix="/")
async def on_ready(self):
  print(f'{self.user.display_name}Est Connecté Au Serveur."")
 = ()
.run(os.getenv("TOKEN")) 

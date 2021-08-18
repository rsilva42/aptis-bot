#!/usr/bin/env python3

import os
import discord
from dotenv import load_dotenv

if __name__ == "__main__":
  pass

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
  print('aptis-bot is online')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  print(message.author)

client.run(os.getenv('TOKEN'))
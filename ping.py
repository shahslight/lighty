# to write up a ping command, you first need to setup your bot correctly with imports such as import discord, import commands and etc.
# here is the code, ignore the text in # okay?

@bot.command(usage="ping", help="Check the bot's ping.")
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
  embed = discord.Embed(
    title='Pong!', color=0x534145,
    description=f'Latency: {bot.latency}ms'
  )
  await ctx.send(embed=embed)
  
  
  
  
  
  
  
  
  
  # here are the imports you need for all of our upcoming sources: you do not need them all nessescarly, but they will be useful in the future.
  # Download them using pip install [variable]
import discord
import random
import asyncio
import copy
import logging
import os
import re
import json
import sys
import aiohttp
import typing
import colorama
from discord import member
from discord.embeds import Embed
from discord.ext.commands.core import command
import requests
from datetime import datetime
import datetime as DateTime
from subprocess import PIPE
from types import SimpleNamespace
from colorama import Fore, Style, init
from discord.ext import commands, tasks
from discord.ext import commands

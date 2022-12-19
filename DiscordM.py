from os import getenv
import requests
import json
import discord
import asyncio
import argparse
import time

client = discord.Client()
parser = argparse.ArgumentParser()

parser.add_argument(
	'--server', 
	'-S',
	type=str, 
	required=False,
	default="127.0.0.1",
	help="domain or IP of your server. (e.g. 127.0.0.1)"
)

parser.add_argument(
	'--port', 
	'-P',
	type=str, 
	required=False,
	default='30120',
	help="port of your server (default: 30120)"
)

parser.add_argument(
	'--timeout', 
	'-T',
	type=int, 
	required=False,
	default='30',
	help="timeout on how often the bot should update (default: 30s)"
)

parser.add_argument(
	'--players', 
	'-Pc',
	type=int, 
	required=False,
	default='64',
	help="max amount of players for your  server (default: 64)"
)

arguments = parser.parse_args()
server_endpoint = f'http://{arguments.server}:{arguments.port}/players.json'

if getenv("DISCORDM") is None:
	exit("[!] DISCORDM environment variable has not been set.")

def get_online_players() -> int:
  response = requests.get(server_endpoint, timeout=3).json()
  return len([data for data in response])

@client.event
async def on_ready():
  print("[i] DiscordM is running!\n")
  print("[i] Authenticated as: {}", end="\n\n".format(client.user))

  await client.change_presence(activity=discord.Game(name='DiscordM Loading'))

async def change():
  await client.wait_until_ready()
  while not client.is_closed():
    current_players = get_online_players()
    current_status = f"Online: {current_players}/{arguments.players}"
    print(f"[i] Online: {current_players}", end="\n\n")

    await client.change_presence(activity=discord.Game(name=current_status))
    await asyncio.sleep(arguments.timeout)

try:
  client.loop.create_task(change())
  client.run(getenv('DISCORDM'))
except discord.errors.LoginFailure:
	exit('[i] Invalid Discord API Token.')

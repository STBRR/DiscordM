from os import getenv
import requests
import json
import discord
import asyncio
import argparse

client = discord.Client()
parser = argparse.ArgumentParser()

parser.add_argument(
	'--server', 
	'-S',
	type=str, 
	required=True,
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

arguments = parser.parse_args()
server_endpoint = f'http://{arguments.server}:{arguments.port}/players.json'

if getenv("DISCORDM") is not None:
	pass
else:
	exit("[!] DISCORDM environment variable has not been set.")

# Iterate over JSON array and parse the count of all players.
def onlinePlayers():
	while(True):
		try:
			response = requests.get(server_endpoint, timeout=5).json()
			online_players = []

			for player in response:
				online_players.append(player['name'])
			return len(online_players)
		except:
			exit(f"[!] Error. Requesting {server_endpoint}. Check your connection.")

@client.event
async def on_ready():
		print("[*] Bot is running!\n")
		print("[*] Authenticated as:" , client.user, end='\n\n')
		await client.change_presence(activity=discord.Game(name='Loading..'))

async def change():
	await client.wait_until_ready()
	while not client.is_closed():
		currentOnline = onlinePlayers()
		currentStatus = 'Online: {}/64'.format(str(currentOnline))

		print("[*] Player(s):", str(currentOnline), end='\r')
		
		await client.change_presence(activity=discord.Game(name=currentStatus))
		await asyncio.sleep(30)

try:
	client.loop.create_task(change())
	client.run(getenv('DISCORDM'))
except:
	exit('[!] Error. Closing down bot.')
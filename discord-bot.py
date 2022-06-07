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

parser.add_argument(
	'--timeout', 
	'-T',
	type=int, 
	required=False,
	default='30',
	help="timeout on how often the bot should update (default: 30s)"
)

arguments = parser.parse_args()
server_endpoint = f'http://{arguments.server}:{arguments.port}/players.json'

if getenv("DISCORDM") is not None:
	pass
else:
	exit("[!] DISCORDM environment variable has not been set.")

# Iterate over JSON array and parse the count of all players.
def onlinePlayers():
	try:
		while(True):
			try:
				response = requests.get(server_endpoint, timeout=5).json()
			except:
				print(f"[!] Error. Requesting {server_endpoint}. Check your connection.")
				exit(0)

			online_players = []

			for player in response:
				online_players.append(player['name'])
			
			return online_players
	except:
		exit()

@client.event
async def on_ready():
		print("[*] Bot is running!\n")
		print("[*] Authenticated as:" , client.user, end='\n\n')
		await client.change_presence(activity=discord.Game(name='Loading..'))

async def change():
	await client.wait_until_ready()
	while not client.is_closed():
		serverData = onlinePlayers()
		currentOnline = len(serverData)
		currentStatus = 'Online: {}/64'.format(str(currentOnline))

		print("[*] Total Player(s):", str(currentOnline), end='\n\n')

		index = 1
		for player in serverData:
			print(str(index) + ":" + player)
			index += 1
		
		await client.change_presence(activity=discord.Game(name=currentStatus))
		await asyncio.sleep(arguments.timeout)

try:
	client.loop.create_task(change())
	time.sleep(1)
	client.run(getenv('DISCORDM'))
	
except discord.errors.LoginFailure:
	exit('Error. Invalid Token. Please Verify and try again.')

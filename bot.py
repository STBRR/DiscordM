import requests
import json
import discord
import asyncio
import os

client = discord.Client()

# Debug Mode
debug = False

endpoint = "http://[IP/Domain]/players.json"

# Iterate over JSON array and parse the count of all players.
def onlinePlayers():
	while(True):
		response = requests.get(endpoint).json()
		online_players = []

		for user in response:
			online_players.append(user['name'])

		return len(online_players)

@client.event
async def on_ready():
		print("[!] Connected Successfully!")
		print("[*] Bot is running!\n")

		if debug:
			print("[+] Logged in as:" , client.user, end='\n\n')
		await client.change_presence(activity=discord.Game(name='Initialized'))

async def change():
	await client.wait_until_ready()
	while not client.is_closed():
		currentOnline = onlinePlayers()
		currentStatus = 'Online: {}/64'.format(str(currentOnline))

		if debug:
			print("[*] Current Player Count:", str(currentOnline), end='\r')
		
		await client.change_presence(activity=discord.Game(name=currentStatus))
		await asyncio.sleep(15)

try:
	client.loop.create_task(change())
	# Place token here or set environment variable with: 'export DISCORD_TOKEN="token_here"
	client.run(os.getenv('DISCORD_TOKEN'))
except:
	exit()

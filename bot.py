import requests
import json
import discord
import asyncio

# Discord Instance.
client = discord.Client()

# players.json endpoint is here
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
		await client.change_presence(activity=discord.Game(name='Initialized'))


async def change():
	await client.wait_until_ready()
	while not client.is_closed():
		currentOnline = onlinePlayers()
		currentStatus = 'Online: {}/64'.format(str(currentOnline))
		
		await client.change_presence(activity=discord.Game(name=currentStatus))
		await asyncio.sleep(2)

client.loop.create_task(change())
client.run(os.getenv('DISCORD_TOKEN'))

## DiscordM (FiveM Server Bot)
*A simple bot for polling your FiveM server endpoint and displaying the current amount of players online.*

### Installation
1. Install the required modules (discord etc..) with:  `pip3 install -r requirements.txt`
2. Execute `export DISCORDM=<token>` to set an environment variable with your bot token

### Usage
1. Head to https://discord.com/developers/ and create a bot
2. Obtain your Token
3. Invite the bot to your server.
4. Run the script with `python3 discord-bot.py -S <IP/Domain>`
5. Your bot should now be online and display a player count.

#### How it works
1. Sends a request to the `players.json` endpoint which is found on pretty much every FiveM Server
2. Parses the JSON array which is returned in the request
3. Iterates though all of the `name` keys
4. Returns the total count of players which are currently online
5. Updates the bots status with how many players are online

#### Screenshot
![](https://i.imgur.com/QxhZ8Zi.png)

*I couldn't really find a simple script that could do as i wanted without too much hassle. A lot of the scripts i found online were written using NodeJS and required some setup so decided to write my own. It's a bit 'hacky' but it does the job!*


### Yamato Discord Bot
A simple discord bot that i wrote for my FiveM server.

_This script does the following:_

1. Sends a request to the `players.json` endpoint which is found on pretty much every FiveM Server
2. Parses the array which is returned in the request
3. Iterates though all of the `name` keys which are within this array
4. Returns the total count of players which are currently online
5. Updates the bots current status with the current amount of online players

I couldn't really find a simple script that could do as i wanted without too much hassle. A lot of the scripts i found online were written using NodeJS and required some setup so decided to write my own. It's a bit 'hacky' but it does the job!

Enjoy.

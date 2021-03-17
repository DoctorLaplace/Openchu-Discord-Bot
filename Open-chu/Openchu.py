import discord
import random




class MyClient(discord.Client):
    global count

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')  


    async def on_message(self, message):
        global count

        if message.author == self.user:
            return

        if message.content == 'Hello Openchu!':
            await message.channel.send("Pika!")







client = MyClient()
client.run('INSERT BOT KEY')
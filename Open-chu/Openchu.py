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




botkey = None
# Place the path to your external botkey text file. This makes sure that Git does not commit your botkey to the open internet!
with open('C:/Users/silve/Desktop/Discord Bots/Openchu/Openchu_Key.txt', 'r') as file:
    botkey = file.read().replace('\n', '')
    print(botkey)

client = MyClient()
client.run(botkey)
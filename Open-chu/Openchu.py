import discord
import random



class MyClient(discord.Client):
    global count


    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')  

        guild = self.get_guild(801480291305783326)
        channel = self.get_channel(801480291305783333)


        pikamood = True
        # pikamood
        if pikamood == True:
            await channel.send("Open-chu uses vibe")
            counter = 0
            messages = await channel.history(limit=50).flatten()
        for i in range(5):
            randomNum = random.randint(1,5)
            randomHistory = random.randint(1,50)
            if randomNum == 1:
                await messages[randomHistory].add_reaction("💖")
            if randomNum == 2:
                await messages[randomHistory].add_reaction("❤")
            if randomNum == 3:
                await messages[randomHistory].add_reaction("💜")
            if randomNum == 4:
                await messages[randomHistory].add_reaction("💛")
            if randomNum == 5:
                await messages[randomHistory].add_reaction("💝")
            

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
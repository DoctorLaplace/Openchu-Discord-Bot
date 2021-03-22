import discord
import random



class dataSocket():
    def __init__(self, data):
        self.data = None

    def setData(self, input):
        self.data = input

    def getData(self):
        return self.data




class BattleArena():

    def __init__(self, player1, player2, pokemon1, pokemon2):
            self.player1 = None
            self.player2 = None

            self.pokemon1 = None
            self.pokemon2 = None

    def setPlayer1(self, p):
        self.player1 = p

    def setPlayer2(self, p):
        self.player2 = p

    def setPokemon(self, pat1, pat2):
        self.pokemon1 = pat1
        self.pokemon2 = pat2





class Pokemon():

    def __init__(self, strength = 0, dexterity = 0, constitution = 0, intelligence = 0, wisdom = 0, charisma = 0, hitpoints = 0, name = "UNDEFINED POKEMON", picture = None):
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10

        self.hitpoints = 100
        self.name = "UNDEFINED POKEMON"
        self.picture = None

    def attack_tackle(self, target, damagePassBack = None):
        target.hitpoints -= self.strength*2
        damagePassBack = self.strength*2

    def getName(self):
        return self.name
    def getHitpoints(self):
        return self.hitpoints




class MyClient(discord.Client):
    global count
    checkPlayer1 = False
    checkPlayer2 = False
    battleZone = BattleArena(None, None, None, None)
    battleActive = False
    battleChannel = None

    playerTurnNum = 1

    player1DataSocket = dataSocket(None)
    player2DataSocket = dataSocket(None)


    pok1 = Pokemon()
    pok1.name = "Shrek"
    battleZone.pokemon1 = pok1
    pok2 = Pokemon()
    pok2.name = "Darmander"
    battleZone.pokemon1 = pok2

    async def displayPokemonStatus(self, channel, pokemon):
        await channel.send(pokemon.getName() + "stats:\n" + str(pokemon.getHitpoints()))


    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')  

        guild = self.get_guild(801480291305783326)
        channel = self.get_channel(801480291305783333)


        pikamood = False
        # pikamood
        if pikamood == True:
            await channel.send("Open-chu uses vibe")
            counter = 0
            messages = await channel.history(limit=50).flatten()
            for i in range(5):
                randomNum = random.randint(1,3)
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

        battlemode = True
        # pikamood
        if message.content == 'Initiate Battle' and battlemode == True:
            await message.channel.send("Players! Are you ready?!")
            self.checkPlayer1 = True
            self.checkPlayer2 = True
            self.battleChannel = message.channel
        
        if message.content == 'I am player 1' and self.checkPlayer1 == True:
            checkPlayer1 = False
            self.battleZone.setPlayer1(message.author)
            await message.channel.send("Player one locked in as " + message.author.name + "!...")

        if message.content == 'I am player 2' and self.checkPlayer2 == True:
            checkPlayer2 = False
            self.battleZone.setPlayer2(message.author)
            await message.channel.send("Player two locked in as " + message.author.name + "!...")


        if message.author == self.battleZone.player1 and self.battleZone.player1 != None:
            self.player1Socket = message.content
            self.player1DataSocket.setData(message.content)
            await message.channel.send("Player one socket is now: " + message.content)


        if message.author == self.battleZone.player2 and self.battleZone.player2 != None:
            self.player2Socket = message.content
            self.player2DataSocket.setData(message.content)
            await message.channel.send("Player two socket is now: " + message.content)



        if message.content == 'Battle Cycle':
            self.battleChannel = message.channel
            self.battleActive = True
            await self.battleThinkCycle()
            print("Program is free now.")

        if message.content == 'End Battle Cycle':
            self.battleActive = False




                     
            
    async def battleThinkCycle(self):
        count = 0
        await self.battleChannel.send("A battle is about to begin between " + self.battleZone.player1.name + " and " + self.battleZone.player1.name + "!...")
        while self.battleActive == True:
            count += 1
            await self.battleChannel.send("Battle heartbeat " + str(count) + " - It is player" + str(self.playerTurnNum) + "'s turn")

            if self.playerTurnNum == 1:
                turnCount = 0
                takenTurn = False
                await self.battleChannel.send(self.battleZone.player1.name + " it is your turn!...")
                while takenTurn == False and self.battleActive == True:
                    turnCount += 1
                    await self.battleChannel.send("Primed")
                    if self.player1DataSocket.getData() == "Shrek use hyperbeam!":
                        await self.battleChannel.send("***Shrek emits a beam of pure destruction!...***")
                        await self.displayPokemonStatus(self.battleChannel,self.battleZone.pokemon1)
                        self.playerTurnNum = 2
                        takenTurn = True
                        self.player1DataSocket.setData(None)


            if self.playerTurnNum == 2:
                turnCount = 0
                takenTurn = False
                await self.battleChannel.send(self.battleZone.player2.name + " it is your turn!...")
                while takenTurn == False and self.battleActive == True:
                    turnCount += 1
                    await self.battleChannel.send("Primed")
                    if self.player2DataSocket.getData() == "Darmander use glock!":
                        await self.battleChannel.send("***Darmander shoots his opponent!...***")
                        self.playerTurnNum = 1
                        takenTurn = True
                        self.player1DataSocket.setData(None)







        await self.battleChannel.send("The battle has ended!...")


        





botkey = None
# Place the path to your external botkey text file. This makes sure that Git does not commit your botkey to the open internet!
with open('C:/Users/silve/Desktop/Discord Bots/Openchu/Openchu_Key.txt', 'r') as file:
    botkey = file.read().replace('\n', '')
    print(botkey)

client = MyClient()
client.run(botkey)
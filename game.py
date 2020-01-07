import random

class Product:

    def __init__(self):
        self.price = random.randint(1,10)
        self.revenue = round(self.price / random.uniform(0.5, 1), 1)
        self.terms = random.randint(1,3)
        self.risk = round(random.random(), 2)

        self.owner = None
        self.roundsRemain = self.terms

    def update(self):

        rand = random.random()
        if rand < self.risk:
            print('BOOM![{:.2f}] {} missed {}! (balance:{})'.format( \
            rand, self.owner.name, self.revenue, self.owner.money))
            self.roundsRemain = -1

        self.roundsRemain -= 1
        if self.roundsRemain == 0:
            self.owner.money += self.revenue
            self.owner.myProduct
            print('{} +{}! (balance:{})'.format(self.owner.name, self.revenue, self.owner.money))

    def display(self):
        print('(Price|{}, Revenue|{}, Terms|{}, Risk|{})'.format( \
        self.price, self.revenue, self.terms, self.risk))

class Player:

    playerNum = 0

    def __init__(self, name):
        self.name = name
        self.money = 10
        self.myProduct = []

        Player.playerNum += 1
        self.id = Player.playerNum

    def __lt__(player1, player2):
        return player1.id < player2.id

    def makeDecision(self, product):
        if product.price > self.money:
            print("{} can't afford it! (balance:{})".format(self.name, self.money))
        else:
            return input(self.name + ' buy? (y/n): ')

    def rollDice(self):
        return random.randint(1,100)

class PlayerRobot(Player):

    def __init__(self):
        name = 'Robot' + str(random.randint(1000,1999))
        super().__init__(name)

    def makeDecision(self, product):
        decision = 'n'
        if product.price < self.money and product.risk < 0.3:
            if random.random() < 0.8:
                decision = 'y'
        print(self.name + ' buy? (y/n): ' + decision)
        return decision

playerList = []
playerList.append(Player('A'))
# playerList.append(Player('B'))
playerList.append(PlayerRobot())
roundCount = 0

while True:

    roundCount += 1

    print('\nRound #' + str(roundCount))

    toEndGame = False
    for player in playerList:
        for product in player.myProduct:
            product.update()
        player.myProduct = [product for product in player.myProduct if product.roundsRemain > 0]
        if player.money <= 0:
            print(player.name + ' Lose!')
            toEndGame = True
        if player.money >=20:
            print(player.name + ' Win!')
            toEndGame = True
    if toEndGame == True:
        print('GAME OVER!!!')
        break

    newProduct = Product()
    newProduct.display()

    shuffleSeq = [(player.rollDice(), player) for player in playerList]
    playerList = [elem[1] for elem in sorted(shuffleSeq, reverse=True)]

    for player in playerList:
        if newProduct.owner != None:
            break

        if len(player.myProduct) < 1:
            decision = player.makeDecision(newProduct)
            if decision == 'y':
                player.myProduct.append(newProduct)
                newProduct.owner = player
                player.money -= newProduct.price
                print('{} -{}! (balance:{})'.format(player.name, newProduct.price, player.money))

from random import choice
from time import sleep

from GameSound import gameSound
from Weapon import weapons
from Potion import potions

GAME_NAME = "FINDING THE CROWN"
BIG_STRING_LENGTH = 100
MEDIUM_STRING_LENGTH = 70
SPECIAL_COMMANDS = ["menu", "weapons", "potions", "exit"]
MAX_WEAPONS = 2
MAX_POTIONS = 50
INITIAL_LIFES = 3
INITIAL_POINTS = 200

class GameUI:

    def __init__(self):
        self.lifes = INITIAL_LIFES
        self.points = INITIAL_POINTS
        self.weapons = [choice(weapons)]
        self.potions = [choice(potions)]
        self.wonnedBattles = 0
        self.state = "menu"
        self.input = None
        self.weaponInHand = self.weapons[0]
        self.hasStarted = False


    def printWithTime(self, message):
        print(message)
        sleep(len(message) * 0.07)


    def askToPlayer(self, message):
        print()
        self.input = input("> " + message + ": ")
        print()
    

    def goToState(self, newState):
        self.state = newState
        self.input = None


    def addLifes(self, lifesToAdd):
        if self.lifes + lifesToAdd > 0:
            if lifesToAdd > 0: self.printWithTime("Has ganado una vida")
            else: self.printWithTime("Has perdido una vida")

            self.lifes += lifesToAdd

        else:
            self.printWithTime("Te has quedado sin vidas, has perdido el juego")
            self.goToState("menu")
    
        self.statsScreen()


    def addPoints(self, pointsToAdd):
        if self.points + pointsToAdd > 0:
            if pointsToAdd > 0: self.printWithTime(f'Has ganado {pointsToAdd} puntos')
            else: self.printWithTime(f'Has perdido {pointsToAdd * -1} puntos')

            self.points += pointsToAdd

        else: self.addLifes(-1)

        self.statsScreen()


    def headerScreen(self, title, type="small"):
        if type == "big":
            spaces = BIG_STRING_LENGTH - len(title)
            left = spaces // 2
            right = spaces - left

            print("-" * BIG_STRING_LENGTH)
            print(f'{" " * left}{title}{" " * right}')
            print("-" * BIG_STRING_LENGTH)
        else:
            print(title.upper())
            print("-" * len(title))


    def menuScreen(self):
        self.headerScreen(GAME_NAME, "big")
        print("1. Jugar")
        print("2. Configuraciones")
        print("3. Reglas del juego")
        print("4. Salir")
        self.askToPlayer("¿Qué quieres hacer?")

        if self.input == "1": self.goToState("game")
        elif self.input == "2": self.goToState("settings")
        elif self.input == "3": self.goToState("rules")
        elif self.input == "4": self.goToState("exit")


    def gameScreen(self):
        if self.hasStarted:
            self.goToState("walk")
        else:
            self.printWithTime("Acabas de despertar en una habitación oscura y sombría")
            self.printWithTime("No recuerdas nada, ni siquiera tu nombre")
            self.printWithTime("De repente observas un cofre con una nota encima de él")
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~   No sabría cómo explicártelo, pero es necesario que en    ~")
            print("~   cuanto despiertes, tomes lo que hay en la caja y vayas   ~")
            print("~   a la montaña en el oriente donde se encuentra el         ~")
            print("~   castillo abandonado. Busca la corona de esmeraldas y     ~")
            print("~   activa su poder para que puedas volver a tu mundo.       ~")
            print("~   Espero que tengas suerte, este mundo es muy peligroso.   ~")
            print("~                                                            ~")
            print("~   Con amor, tu madre.                                      ~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            sleep(10)
            print("Abres la caja...")
            gameSound.playOpenChest()
            self.printWithTime("Observas un arma y una poción")
            self.printWithTime(f'El arma es {self.weapons[0].usedName} {self.weapons[0].emoji}')
            self.printWithTime(f'La poción tiene una etiqueta que dice "{self.potions[0].name} {self.potions[0].emoji}"')
            self.printWithTime("Te pones en pie y te diriges a la puerta")
            print("Abres la puerta...")
            gameSound.playOpenDoor()
            self.printWithTime("Observas un pequeño pasillo oscuro")
            self.printWithTime("Te percatas que no hay nadie más en esa pequeña casa")
            self.printWithTime("Sales de la casa")

            self.hasStarted = True


    def walk(self):
        print("Vas caminando...")
        gameSound.playWalk()

        option = choice(["battle", "potion", "nothing"])

        if option == "battle": self.goToState("battle")
        elif option == "potion": self.goToState("found-potion")
        elif option == "nothing": self.goToState("walk")


    def settingsScreen(self):
        self.headerScreen("Configuraciones")
        print(f'1. Volumen de la música - {gameSound.musicVolume}%')
        print(f'2. Volumen de los efectos de sonido - {gameSound.soundVolume}%')
        print("3. Volver al menú")
        self.askToPlayer("¿Qué quieres hacer?")

        if self.input == "1": self.goToState("music-settings")
        elif self.input == "2": self.goToState("sound-settings")
        elif self.input == "3": self.goToState("menu")


    def musicSettingsScreen(self):
        self.headerScreen("Configuraciones de la música")
        self.askToPlayer("¿Qué volumen quieres ponerle a la música? (0 - 100)")

        if float(self.input) >= 0 and float(self.input) <= 100:
            gameSound.setMusicVolume(float(self.input))
            self.goToState("settings")


    def soundSettingsScreen(self):
        self.headerScreen("Configuraciones de los efectos de sonido")
        self.askToPlayer("¿Qué volumen quieres ponerle a los efectos de sonido? (0 - 100)")

        if float(self.input) >= 0 and float(self.input) <= 5:
            gameSound.setSoundVolume(float(self.input))
            self.goToState("settings")

    def rulesScreen(self):
        self.headerScreen("Reglas del juego")
        print(f'¡Bienvenido a {GAME_NAME}!')
        print("En esta aventura deberás enfrentarte a diferentes enemigos para sobrevivir en el juego.")
        print("Tu objetivo principal es buscar la corona perdida, que se encuentra en el castillo de la montaña.") 
        print("Pero para llegar allí deberás vencer a los enemigos que se encuentran en el camino.")
        print("Cada vez que ganes una batalla podrás tomar el arma del enemigo.")
        print(f'Puedes guardar hasta {MAX_WEAPONS} armas y {MAX_POTIONS} pociones. Cada arma tiene un daño diferente.')
        print(f'Comienzas el juego con {INITIAL_LIFES} vidas, {INITIAL_POINTS} puntos, un arma y una pocion aleatorias.')
        self.askToPlayer("Presiona ENTER para volver al menú")

        if self.input == "": self.goToState("menu")


    def statsScreen(self):
        print("~" * MEDIUM_STRING_LENGTH)
        print(f'❤️  Vidas: {self.lifes}', end=" " * 5)
        print(f'⭐ Puntos: {self.points}', end=" " * 5)
        print(f'⚔️  Batallas ganadas: {self.wonnedBattles}')
        print("~" * MEDIUM_STRING_LENGTH)
    

    def weaponsScreen(self):
        n = len(self.weapons)
        availablePositions = [str(i + 1) for i in range(n)]
        self.headerScreen("Armas")

        for i in range(n):
            weapon = self.weapons[i]
            print(f'{i + 1}. {weapon.name} {weapon.emoji} (Daño: {weapon.damage})')
        
        print("Ingresa el número del arma que quieres llevar en las manos o presiona ENTER para volver atrás")
        self.askToPlayer("¿Qué quieres hacer?")

        if self.input == "": self.goToState("walk")
        elif self.input in availablePositions:
            self.weaponInHand = self.weapons[int(self.input) - 1]
            print(f'Has elegido {self.weaponInHand.usedName} {self.weaponInHand.emoji}')

            self.askToPlayer("Presiona ENTER para volver atrás")
            if self.input == "": self.goToState("walk")
            elif self.input in SPECIAL_COMMANDS: self.goToState(self.input)
        elif self.input in SPECIAL_COMMANDS: self.goToState(self.input)

    
    def potionsScreen(self):
        n = len(self.potions)
        availablePositions = [str(i + 1) for i in range(n)]
        self.headerScreen("Pociones")

        if n == 0:
            print("No tienes pociones")
            self.askToPlayer("Presiona ENTER para volver atrás")
            if self.input == "": self.goToState("walk")
            elif self.input in SPECIAL_COMMANDS: self.goToState(self.input)
        else:
            for i in range(n):
                potion = self.potions[i]
                print(f'{i + 1}. {potion.name} {potion.emoji} ({potion.description})')
            
            print("Ingresa el número de la poción que quieres beber o presiona ENTER para volver atrás")
            self.askToPlayer("¿Qué quieres hacer?")

            if self.input == "": self.goToState("walk")
            elif self.input in availablePositions:
                potionToDrink = self.potions[int(self.input) - 1]
                self.potions.pop(int(self.input) - 1)
                print(f'Bebiendo la poción {potionToDrink.name} {potionToDrink.emoji}')
                gameSound.playOpenPotion()
                self.printWithTime(potionToDrink.message)

                if potionToDrink.name == "Fenix": self.addLifes(potionToDrink.value)
                elif potionToDrink.name == "Poder": self.addPoints(potionToDrink.value)
                elif potionToDrink.name == "Suerte de los dioses": self.addPoints(potionToDrink.value)
                elif potionToDrink.name == "Oportunidad": self.addPoints(potionToDrink.value)

                self.askToPlayer("Presiona ENTER para volver atrás")
                if self.input == "": self.goToState("walk")
                elif self.input in SPECIAL_COMMANDS: self.goToState(self.input)
            elif self.input in SPECIAL_COMMANDS: self.goToState(self.input)


    def saveWeapon(self, newWeapon):
        n = len(self.weapons)
        availablePositions = [str(i + 1) for i in range(n)]

        if n < MAX_WEAPONS:
            self.weapons.append(newWeapon)
            print(f'Has guardado {newWeapon.usedName} {newWeapon.emoji}')
        else:
            print("No tienes espacio para guardar más armas, debes elegir una para reemplazar")

            for i in range(n):
                weapon = self.weapons[i]
                print(f'{i + 1}. {weapon.name} {weapon.emoji} (daño: {weapon.damage})')

            self.askToPlayer("¿Qué arma quieres reemplazar? (ENTER para cancelar)")

            if self.input == "": self.goToState("walk")
            elif self.input in availablePositions:
                oldWeapon = self.weapons[int(self.input) - 1]
                print(f'Has reemplazado {oldWeapon.usedName} {oldWeapon.emoji} por {newWeapon.usedName} {newWeapon.emoji}')
                self.weapons[int(self.input) - 1] = newWeapon
            elif self.input in SPECIAL_COMMANDS: self.goToState(self.input)


    def foundPotion(self):
        n = len(self.potions)
        availablePositions = [str(i + 1) for i in range(n)]

        newPotion = choice(potions)
        print(f'Has encontrado la poción "{newPotion.name} {newPotion.emoji}" ({newPotion.description})')
        self.askToPlayer("¿Quieres guardarla? (s/n)")

        if self.input == "S" or self.input == "s":
            if n < MAX_POTIONS:
                self.potions.append(newPotion)
                print(f'Has guardado la poción {newPotion.name} {newPotion.emoji}')
            else:
                print("No tienes espacio para guardar más pociones, debes elegir una para reemplazar")

                for i in range(n):
                    potion = self.potions[i]
                    print(f'{i + 1}. {potion.name} {potion.emoji} ({potion.description})')
                
                self.askToPlayer("¿Qué poción quieres reemplazar? (ENTER para cancelar)")

                if self.input == "": self.goToState("walk")
                elif self.input in availablePositions:
                    oldPotion = self.potions[int(self.input) - 1]
                    print(f'Has reemplazado la poción {oldPotion.name} {oldPotion.emoji} por {newPotion.name} {newPotion.emoji}')
                    self.potions[int(self.input) - 1] = newPotion
                elif self.input in SPECIAL_COMMANDS: self.goToState(self.input)
        elif self.input == "N" or self.input == "n":
            print("Dejas la poción en el suelo")
        elif self.input in SPECIAL_COMMANDS:
            command = self.input
            self.goToState(command)

        self.goToState("walk")


    def battle(self):
        enemyWeapon = choice(weapons)
        myWeapon = self.weaponInHand

        self.printWithTime(f'Alguien te ha atacado con {enemyWeapon.usedName} {enemyWeapon.emoji}')

        direction = choice(["left", "right"])
        gameSound.playScream(direction)
        print("¿Hacia dónde quieres atacar?")
        print("1. Izquierda")
        print("2. Derecha")
        self.askToPlayer("Elige una opción")

        if self.input == "1" or self.input == "2":
            self.printWithTime(f'Atacando con {myWeapon.usedName} {myWeapon.emoji}')

            if (self.input == "1" and direction == "left") or (self.input == "2" and direction == "right"):
                win = myWeapon.damage >= enemyWeapon.damage
            else:
                win = False

            if win:
                print("Has ganado esta batalla 😎")
                gameSound.playWin()
                self.addPoints(myWeapon.damage)
                self.wonnedBattles += 1
    
                self.askToPlayer("¿Quieres guardar el arma? (s/n)")

                if self.input == "S" or self.input == "s": self.saveWeapon(enemyWeapon)
                elif self.input == "N" or self.input == "n": self.printWithTime(f'Has dejado {enemyWeapon.usedName} en el suelo')
                elif self.input in SPECIAL_COMMANDS: self.goToState(self.input)

            else:
                print("Has perdido esta batalla ☹️")
                gameSound.playLose()
                self.addPoints(-enemyWeapon.damage)

            if self.wonnedBattles == 10: self.finalBattle()
            else: self.walk()

        elif self.input in SPECIAL_COMMANDS: self.goToState(self.input)


    def finalBattle(self):
        self.printWithTime("Por fin has llegado al castillo de la montaña")
        self.printWithTime("De repente una voz detrás tuyo te sobresalta:")
        self.printWithTime("")
        self.printWithTime("   Te he estado esperando, estaba seguro que llegarías hasta aquí")
        self.printWithTime("   Ella te dio y te dijo lo necesario para volver a tu mundo")
        self.printWithTime("   Pero por supuesto, nunca te dijo quién te esperaría aquí")
        self.printWithTime("   Apuesto a que ni siquiera sabes quién es ella")
        self.printWithTime("   Apuesto a que ni siquiera sabes quién eres")
        self.printWithTime("   Pero no te preocupes, yo te lo diré, eso no importa")
        self.printWithTime("   En este mundo glorioso para mí, no voy a permitir que ganes")
        self.printWithTime("")
        self.printWithTime("Tu enemigo saca su mejor arma y te ataca")

        myWeapon = self.weaponInHand

        self.printWithTime(f'Atacando con {myWeapon.usedName}')
        win = choice([True, False])

        if win:
            print("Has ganado el juego 😎")
            gameSound.playWin()
            self.goToState("menu")
        else:
            print("Has perdido el juego ☹️")
            gameSound.playGameOver()
            self.goToState("menu")

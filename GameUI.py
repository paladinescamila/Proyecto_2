from sys import exit
from random import choice
from time import sleep

from GameSound import sound
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
BATTLES_WON_BEFORE_FINAL_BATTLE = 10

class GameUI:

    def __init__(self):
        self.lifes = INITIAL_LIFES
        self.points = INITIAL_POINTS
        self.weapons = [choice(weapons)]
        self.potions = [choice(potions)]
        self.wonnedBattles = 0
        self.weaponInHand = self.weapons[0]
        self.hasStarted = False
        self.menuScreen()


    def printWithTime(self, message):
        print(message)
        sleep(len(message) * 0.07)


    def askToPlayer(self, message):
        print()
        value = input("> " + message + ": ")
        print()
        return value

    
    def executeCommand(self, command):
        if (command == "menu"): self.menuScreen()
        elif (command == "weapons"): self.weaponsScreen()
        elif (command == "potions"): self.potionsScreen()
        elif (command == "exit"): exit()


    def addLifes(self, lifesToAdd):
        if self.lifes + lifesToAdd > 0:
            if lifesToAdd > 0: self.printWithTime("Has ganado una vida")
            else: self.printWithTime("Has perdido una vida")

            self.lifes += lifesToAdd

        else:
            self.printWithTime("Te has quedado sin vidas, has perdido el juego")
            self.menuScreen()


    def addPoints(self, pointsToAdd):
        if self.points + pointsToAdd > 0:
            if pointsToAdd > 0: self.printWithTime(f'Has ganado {pointsToAdd} puntos')
            else: self.printWithTime(f'Has perdido {pointsToAdd * -1} puntos')

            self.points += pointsToAdd

        else:
            self.points = 0
            self.addLifes(-1)

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
        sound.playMenuMusic()
        self.headerScreen(GAME_NAME, "big")
        print("1. Jugar")
        print("2. Configuraciones")
        print("3. Salir")
        option = self.askToPlayer("Elige una opción")

        if option == "1": self.gameScreen()
        elif option == "2": self.settingsScreen()
        elif option == "3": exit()
        else: self.menuScreen()


    def gameScreen(self):
        sound.playPlayingMusic()
        if not self.hasStarted:
            self.printWithTime("Acabas de despertar en una habitación oscura y sombría")
            self.printWithTime("No recuerdas nada, ni siquiera tu nombre")
            self.printWithTime("De repente observas un cofre con una nota encima de él")
            print()
            print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
            print("~  No sabría cómo explicártelo, pero es necesario que en    ~")
            print("~  cuanto despiertes, tomes lo que hay en la caja y vayas   ~")
            print("~  a la montaña en el oriente donde se encuentra el         ~")
            print("~  castillo abandonado. Busca la corona de esmeraldas y     ~")
            print("~  activa su poder para que puedas volver a tu mundo.       ~")
            print("~  Espero que tengas suerte, este mundo es muy peligroso.   ~")
            print("~                                                           ~")
            print("~  Con amor, tu madre.                                      ~")
            print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
            print()
            sleep(10)
            print("Abres la caja...")
            sound.playOpenChest()
            self.printWithTime("Observas un arma y una poción")
            self.printWithTime(f'El arma es {self.weapons[0].usedName} {self.weapons[0].emoji}')
            self.printWithTime(f'La poción tiene una etiqueta que dice "{self.potions[0].name} {self.potions[0].emoji}"')
            print("Te pones en pie y te diriges a la puerta")
            sound.playWalk()
            print("Abres la puerta...")
            sound.playOpenDoor()
            self.printWithTime("Observas un pequeño pasillo oscuro")
            self.printWithTime("Te percatas que no hay nadie más en esa pequeña casa")
            self.printWithTime("Sales de la casa")

            self.hasStarted = True
            self.walk()


    def walk(self):
        print("Vas caminando...")
        sound.playWalk()
        option = choice(["battle", "potion", "nothing"])

        if option == "battle": self.battle()
        elif option == "potion": self.foundPotion(choice(potions))

        self.walk()


    def settingsScreen(self):
        self.headerScreen("Configuraciones")
        print(f'1. Volumen de la música - {sound.musicVolume}%')
        print(f'2. Volumen de los efectos de sonido - {sound.soundVolume}%')
        print("3. Volver al menú")
        option = self.askToPlayer("Elige una opción")

        if option == "1": self.musicSettingsScreen()
        elif option == "2": self.soundSettingsScreen()
        elif option == "3": self.menuScreen()
        else: self.settingsScreen()


    def musicSettingsScreen(self):
        self.headerScreen("Configuraciones de la música")
        volume = self.askToPlayer("Introduce el volumen de la música (0-100)")

        if float(volume) >= 0 and float(volume) <= 100:
            sound.setMusicVolume(float(volume))
            self.settingsScreen()
        else: self.musicSettingsScreen()


    def soundSettingsScreen(self):
        self.headerScreen("Configuraciones de los efectos de sonido")
        volume = self.askToPlayer("Introduce el volumen de los efectos de sonido (0-100)")

        if float(volume) >= 0 and float(volume) <= 5:
            sound.setSoundVolume(float(volume))
            self.settingsScreen()
        else: self.soundSettingsScreen()


    def statsScreen(self):
        lifesText = f'❤️  Vidas: {self.lifes}'
        pointsText = f'⭐ Puntos: {self.points}'
        wonnedBattlesText = f'🏆  Batallas ganadas: {self.wonnedBattles}'
        fullText = f'{lifesText}     {pointsText}     {wonnedBattlesText}'
        self.headerScreen(fullText, "big")
    

    def weaponsScreen(self):
        n = len(self.weapons)
        availablePositions = [str(i + 1) for i in range(n)]
        self.headerScreen("Armas")

        for i in range(n):
            weapon = self.weapons[i]
            print(f'{i + 1}. {weapon.name} {weapon.emoji} (Daño: {weapon.damage})')
        
        print(f'Arma en las manos: {self.weaponInHand.name} {self.weaponInHand.emoji}')
        print("Ingresa el número del arma que quieres llevar en las manos o presiona cualquier otra tecla para cancelar")

        while True:
            position = self.askToPlayer("Elige una opción")

            if position in SPECIAL_COMMANDS: self.executeCommand(position)
            else:
                if position in availablePositions:
                    self.weaponInHand = self.weapons[int(position) - 1]
                    print(f'Has elegido {self.weaponInHand.usedName} {self.weaponInHand.emoji}')

                    option = self.askToPlayer("Presiona cualquier tecla para volver atrás")
                    if option in SPECIAL_COMMANDS: self.executeCommand(option)
                else: print("No seleccionaste un arma")
                return

    
    def potionsScreen(self):
        n = len(self.potions)
        availablePositions = [str(i + 1) for i in range(n)]
        self.headerScreen("Pociones")

        if n == 0:
            print("No tienes pociones")
            option = self.askToPlayer("Presiona cualquier tecla para volver atrás")
            if option in SPECIAL_COMMANDS: self.executeCommand(option)
        else:
            for i in range(n):
                potion = self.potions[i]
                print(f'{i + 1}. {potion.name} {potion.emoji} ({potion.description})')
            
            print("Ingresa el número de la poción que quieres beber o presiona cualquier tecla para volver atrás")

            while True:
                position = self.askToPlayer("Elige una opción")

                if position in SPECIAL_COMMANDS: self.executeCommand(position)
                else:            
                    if position in availablePositions:
                        potionToDrink = self.potions[int(position) - 1]
                        self.potions.pop(int(position) - 1)
                        print(f'Bebiendo la poción {potionToDrink.name} {potionToDrink.emoji}')
                        sound.playOpenPotion()
                        self.printWithTime(potionToDrink.message)

                        if potionToDrink.name == "Fenix": self.addLifes(potionToDrink.value)
                        elif potionToDrink.name == "Poder": self.addPoints(potionToDrink.value)
                        elif potionToDrink.name == "Suerte de los dioses": self.addPoints(potionToDrink.value)
                        elif potionToDrink.name == "Oportunidad": self.addPoints(potionToDrink.value)

                        option = self.askToPlayer("Presiona cualquier tecla para volver atrás")
                        if option in SPECIAL_COMMANDS: self.executeCommand(option)
                    else: print("No seleccionaste una poción")
                    return


    def saveWeapon(self, newWeapon):
        n = len(self.weapons)
        availablePositions = [str(i + 1) for i in range(n)]

        while True:
            option = self.askToPlayer("¿Quieres guardar el arma? (s/N)")

            if option in SPECIAL_COMMANDS: self.executeCommand(option)
            else:
                if option == "S" or option == "s":
                    if n < MAX_WEAPONS:
                        self.weapons.append(newWeapon)
                        print(f'Has guardado {newWeapon.usedName} {newWeapon.emoji}')
                    else:
                        print("No tienes espacio para guardar más armas, debes elegir una para reemplazar")

                        for i in range(n):
                            weapon = self.weapons[i]
                            print(f'{i + 1}. {weapon.name} {weapon.emoji} (daño: {weapon.damage})')

                        while True:
                            position = self.askToPlayer("¿Qué arma quieres reemplazar? (cualquier otra tecla para cancelar)")

                            if position in SPECIAL_COMMANDS: self.executeCommand(position)
                            else:
                                if position in availablePositions:
                                    oldWeapon = self.weapons[int(position) - 1]
                                    print(f'Has reemplazado {oldWeapon.usedName} {oldWeapon.emoji} por {newWeapon.usedName} {newWeapon.emoji}')
                                    self.weapons[int(position) - 1] = newWeapon
                                else: print("Dejas la arma en el suelo")
                                return
                else: print("Dejas el arma en el suelo")
                return


    def foundPotion(self, newPotion):
        n = len(self.potions)
        availablePositions = [str(i + 1) for i in range(n)]

        print(f'Has encontrado la poción "{newPotion.name} {newPotion.emoji}" ({newPotion.description})')

        while True:
            option = self.askToPlayer("¿Quieres guardarla? (s/N)")

            if option in SPECIAL_COMMANDS: self.executeCommand(option)
            else:
                if option == "S" or option == "s":
                    if n < MAX_POTIONS:
                        self.potions.append(newPotion)
                        print(f'Has guardado la poción {newPotion.name} {newPotion.emoji}')
                    else:
                        print("No tienes espacio para guardar más pociones, debes elegir una para reemplazar")

                        for i in range(n):
                            potion = self.potions[i]
                            print(f'{i + 1}. {potion.name} {potion.emoji} ({potion.description})')
                        
                        while True:
                            position = self.askToPlayer("¿Qué poción quieres reemplazar? (cualquier otra tecla para cancelar)")

                            if position in SPECIAL_COMMANDS: self.executeCommand(position)
                            else:
                                if position in availablePositions:
                                    oldPotion = self.potions[int(position) - 1]
                                    print(f'Has reemplazado la poción {oldPotion.name} {oldPotion.emoji} por {newPotion.name} {newPotion.emoji}')
                                    self.potions[int(position) - 1] = newPotion
                                else: print("Dejas la poción en el suelo")
                                return
                else:
                    print("Dejas la poción en el suelo")
                return


    def battle(self):
        enemyWeapon = choice(weapons)
        myWeapon = self.weaponInHand
        print(f'Alguien te va a atacar con {enemyWeapon.usedName} {enemyWeapon.emoji}')
        direction = choice(["left", "right"])
        sound.playScream(direction)

        while True:
            playerDirection = self.askToPlayer("¿Quieres atacar a la (I)zquierda o a la (d)erecha?")

            if playerDirection in SPECIAL_COMMANDS: self.executeCommand(playerDirection)
            else:
                if playerDirection in ["I", "i"]: playerDirection, playerDirectionName = "left", "izquierda"
                elif playerDirection in ["D", "d"]: playerDirection, playerDirectionName = "right", "derecha"
                else: playerDirection, playerDirectionName = "left", "izquierda"
                
                self.printWithTime(f'Atacando hacia la {playerDirectionName} con {myWeapon.usedName} {myWeapon.emoji}')

                if (playerDirection == direction): win = myWeapon.damage >= enemyWeapon.damage
                else: win = False

                if win:
                    print("Has ganado esta batalla 😎")
                    sound.playWin()
                    self.wonnedBattles += 1
                    self.addPoints(myWeapon.damage)
                    self.saveWeapon(enemyWeapon)
                else:
                    print("Has perdido esta batalla ☹️")
                    sound.playLose()
                    self.addPoints(-enemyWeapon.damage)

                if self.wonnedBattles == BATTLES_WON_BEFORE_FINAL_BATTLE:
                    return self.finalBattle()
                return


    def finalBattle(self):
        sound.playFinalBattleMusic()
        self.printWithTime("Por fin has llegado al castillo de la montaña")
        self.printWithTime("De repente una voz detrás tuyo te sobresalta:")
        self.printWithTime("")
        self.printWithTime(" - Te he estado esperando, estaba seguro que llegarías hasta aquí")
        self.printWithTime(" - Ella te dio y te dijo lo necesario para volver a tu mundo")
        self.printWithTime(" - Pero por supuesto, nunca te dijo quién te esperaría aquí")
        self.printWithTime(" - Apuesto a que ni siquiera sabes quién es ella")
        self.printWithTime(" - Apuesto a que ni siquiera sabes quién eres")
        self.printWithTime(" - Pero no te preocupes, yo te lo diré, eso no importa")
        self.printWithTime(" - En este mundo glorioso para mí, no voy a permitir que ganes")
        self.printWithTime("")
        self.printWithTime("Tu enemigo saca su mejor arma y te ataca")

        while True:
            option = self.askToPlayer("Presiona cualquier tecla para atacar")

            if option in SPECIAL_COMMANDS: self.executeCommand(option)
            else:
                self.printWithTime(f'Atacando con {self.weaponInHand.usedName}')
                win = choice([True, False])

                if win:
                    sound.playWinGameMusic()
                    print("Has ganado contra tu enemigo 😎")
                    sound.playWin()
                    self.printWithTime("Finalmente lo has derrotado y ahora te diriges al interior del castillo")
                    sound.playWalk()
                    self.printWithTime("Al entrar en la habitación principal encuentras la corona")
                    self.printWithTime("La tomas en tus manos y tocas el rubí que está en su centro")
                    self.printWithTime("De repente te sientes débil y caes al suelo")
                    self.printWithTime("Te despiertas en tu cama, todo ha sido un sueño")

                    self.__init__()
                    self.menuScreen()
                else:
                    sound.playLoseGameMusic()
                    print("Has perdido contra tu enemigo ☹️")
                    sound.playGameOver()
                    self.printWithTime("Caes al suelo, dando tu último aliento")
                    self.printWithTime("Tu enemigo te observa con una sonrisa y te dice:")
                    self.printWithTime(" - No eres digno de la corona, pero no te preocupes, volverás a intentarlo")
                    self.printWithTime("Te despiertas en tu cama, todo ha sido un sueño")
                    self.__init__()
                    self.menuScreen()
                return

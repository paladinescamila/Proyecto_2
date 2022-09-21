from sys import exit
from openal import oalQuit
from random import choice
from time import sleep

from GameSound import sound
from Weapon import weapons
from Potion import potions

GAME_NAME = "FINDING THE CROWN"
BIG_STRING_LENGTH = 100
MEDIUM_STRING_LENGTH = 70
SPECIAL_COMMANDS = ["menu", "weapons", "potions", "exit"]
MAX_WEAPONS = 3
MAX_POTIONS = 10
INITIAL_LIFES = 3
INITIAL_POINTS = 200
BATTLES_WON_BEFORE_FINAL_BATTLE = 10
POSIBLE_VOLUME = [str(i) for i in range(101)]

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


    # Imprime un mensaje con un tiempo de espera
    def printWithTime(self, message):
        print(message)
        sleep(len(message) * 0.07)


    # Pide al jugador que ingrese una opción
    def askToPlayer(self, message):
        print()
        value = input("> " + message + ": ")
        print()
        return value


    # Ejecuta uno de los comandos especiales
    def executeCommand(self, command):
        if (command == "menu"): self.menuScreen()
        elif (command == "weapons"): self.weaponsScreen()
        elif (command == "potions"): self.potionsScreen()
        elif (command == "exit"): exit()


    # Actualiza las vidas del jugador
    def addLifes(self, lifesToAdd):
        if self.lifes + lifesToAdd > 0:
            if lifesToAdd > 0: self.printWithTime("Has ganado una vida")
            else: self.printWithTime("Has perdido una vida")

            self.lifes += lifesToAdd

        else:
            self.printWithTime("Te has quedado sin vidas, has perdido el juego")
            self.menuScreen()


    # Actualiza los puntos del jugador
    def addPoints(self, pointsToAdd):
        if self.points + pointsToAdd > 0:
            if pointsToAdd > 0: self.printWithTime(f'Has ganado {pointsToAdd} puntos')
            else: self.printWithTime(f'Has perdido {pointsToAdd * -1} puntos')

            self.points += pointsToAdd

        else:
            self.points = 0
            self.addLifes(-1)

        self.statsScreen()


    # Crea un titulo para la pantalla
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


    # Muestra la pantalla del menú
    def menuScreen(self):
        sound.playMenuMusic()
        self.headerScreen(GAME_NAME, "big")
        print("1. Jugar")
        print("2. Configuraciones")
        print("3. Salir")
        option = self.askToPlayer("Elige una opción")

        if option == "1": self.gameScreen()
        elif option == "2": self.settingsScreen()
        elif option == "3": oalQuit() ; exit()
        else: self.menuScreen()


    # Muestra la pantalla de la historia
    def gameScreen(self):
        sound.playPlayingMusic()

        if not self.hasStarted:
            self.printWithTime("Acabas de despertar en una habitación oscura y sombría")
            self.printWithTime("No recuerdas nada, ni siquiera tu nombre")
            self.printWithTime("De repente observas un cofre con una nota encima de él")
            print()
            print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
            print("~                                                             ~")
            print("~   No sabría cómo explicártelo, pero es necesario que en     ~")
            print("~   cuanto despiertes, tomes lo que hay en el cofre y vayas   ~")
            print("~   a la montaña en el oriente donde se encuentra el          ~")
            print("~   castillo abandonado. Busca la corona con el rubí y        ~")
            print("~   activa su poder para que puedas volver a tu mundo.        ~")
            print("~   Espero que tengas suerte, este lugar es muy peligroso.    ~")
            print("~                                                             ~")
            print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
            print()
            sleep(10)
            print("Abres el cofre...")
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


    # Muestra la pantalla de cuando el jugador camina
    def walk(self):
        print("Vas caminando...")
        sound.playWalk()
        option = choice(["battle", "potion", "nothing"])

        if option == "battle": self.battle()
        elif option == "potion": self.foundPotion(choice(potions))

        self.walk()


    # Muestra la pantalla de las configuraciones
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


    # Muestra la pantalla de las configuraciones de la música
    def musicSettingsScreen(self):
        self.headerScreen("Configuraciones de la música")
        volume = self.askToPlayer("Ingresa el volumen de la música (0 - 100)")

        if volume in POSIBLE_VOLUME:
            sound.setMusicVolume(int(volume))
            self.settingsScreen()
        else: self.musicSettingsScreen()


    # Muestra la pantalla de las configuraciones de los efectos de sonido
    def soundSettingsScreen(self):
        self.headerScreen("Configuraciones de los efectos de sonido")
        volume = self.askToPlayer("Ingresa el volumen de los efectos de sonido (0 - 100)")

        if volume in POSIBLE_VOLUME:
            sound.setSoundVolume(int(volume))
            self.settingsScreen()
        else: self.soundSettingsScreen()


    # Muestra la pantalla de las estadísticas (puntos, vidas, etc.)
    def statsScreen(self):
        lifesText = f'❤️  Vidas: {self.lifes}'
        pointsText = f'⭐ Puntos: {self.points}'
        wonnedBattlesText = f'🏆  Batallas ganadas: {self.wonnedBattles}'
        fullText = f'{lifesText}     {pointsText}     {wonnedBattlesText}'
        self.headerScreen(fullText, "big")


    # Muestra la pantalla de las armas
    def weaponsScreen(self):
        n = len(self.weapons)
        availablePositions = [str(i + 1) for i in range(n)]
        self.headerScreen("Armas")

        for i in range(n):
            weapon = self.weapons[i]
            print(f'{i + 1}. {weapon.name} {weapon.emoji} (daño: {weapon.damage})')
        
        print(f'Arma en las manos: {self.weaponInHand.name} {self.weaponInHand.emoji}')
        print("Ingresa el número del arma que quieres llevar en las manos o presiona ENTER para cancelar")

        while True:
            position = self.askToPlayer("Elige una opción")

            if position in SPECIAL_COMMANDS: self.executeCommand(position)
            elif position in availablePositions:
                self.weaponInHand = self.weapons[int(position) - 1]
                self.printWithTime(f'Has elegido {self.weaponInHand.usedName} {self.weaponInHand.emoji} para llevar en las manos')

                option = self.askToPlayer("Presiona ENTER para volver atrás")
                if option in SPECIAL_COMMANDS: self.executeCommand(option)
                return


    # Muestra la pantalla de las pociones    
    def potionsScreen(self):
        n = len(self.potions)
        availablePositions = [str(i + 1) for i in range(n)]
        self.headerScreen("Pociones")

        if n == 0:
            print("No tienes pociones")
            option = self.askToPlayer("Presiona ENTER para volver atrás")
            if option in SPECIAL_COMMANDS: self.executeCommand(option)
        else:
            for i in range(n):
                potion = self.potions[i]
                print(f'{i + 1}. {potion.name} {potion.emoji} ({potion.description})')
            
            print("Ingresa el número de la poción que quieres beber o presiona ENTER para volver atrás")

            while True:
                position = self.askToPlayer("Elige una opción")

                if position in SPECIAL_COMMANDS: self.executeCommand(position)
                elif position in availablePositions:
                    sound.playOpenPotion()
                    potionToDrink = self.potions[int(position) - 1]
                    self.potions.pop(int(position) - 1)
                    print(f'Bebiendo la poción "{potionToDrink.name} {potionToDrink.emoji}"')
                    self.printWithTime(potionToDrink.message)

                    if potionToDrink.name == "Fenix": self.addLifes(potionToDrink.value)
                    elif potionToDrink.name == "Poder": self.addPoints(potionToDrink.value)
                    elif potionToDrink.name == "Suerte de los dioses": self.addPoints(potionToDrink.value)
                    elif potionToDrink.name == "Oportunidad": self.addPoints(potionToDrink.value)

                    option = self.askToPlayer("Presiona ENTER para volver atrás")
                    if option in SPECIAL_COMMANDS: self.executeCommand(option)
    
                    return


    # Muestra la pantalla de cuando el jugador guarda un arma
    def saveWeapon(self, newWeapon):
        n = len(self.weapons)
        availablePositions = [str(i + 1) for i in range(n)]

        while True:
            option = self.askToPlayer("¿Quieres guardar el arma? (s/N)")

            if option in SPECIAL_COMMANDS: self.executeCommand(option)
            else:
                if option in ["S", "s"]:
                    if n < MAX_WEAPONS:
                        self.weapons.append(newWeapon)
                        self.printWithTime(f'Has guardado {newWeapon.usedName} {newWeapon.emoji}')
                    else:
                        print("No tienes espacio para guardar más armas, debes elegir una para reemplazar")

                        for i in range(n):
                            weapon = self.weapons[i]
                            print(f'{i + 1}. {weapon.name} {weapon.emoji} (daño: {weapon.damage})')

                        while True:
                            position = self.askToPlayer("¿Qué arma quieres reemplazar? (ENTER para cancelar)")

                            if position in SPECIAL_COMMANDS: self.executeCommand(position)
                            else:
                                if position in availablePositions:
                                    oldWeapon = self.weapons[int(position) - 1]
                                    self.weapons[int(position) - 1] = newWeapon
                                    self.printWithTime(f'Has reemplazado {oldWeapon.usedName} {oldWeapon.emoji} por {newWeapon.usedName} {newWeapon.emoji}')
                                else: self.printWithTime("Dejas la arma en el suelo")
                                return
                else: self.printWithTime("Dejas el arma en el suelo")
                return


    # Muestra la pantalla de cuando el jugador encuentra una poción
    def foundPotion(self, newPotion):
        n = len(self.potions)
        availablePositions = [str(i + 1) for i in range(n)]

        self.printWithTime(f'Has encontrado la poción "{newPotion.name} {newPotion.emoji}"')

        while True:
            option = self.askToPlayer("¿Quieres guardarla? (s/N)")

            if option in SPECIAL_COMMANDS: self.executeCommand(option)
            else:
                if option in ["S", "s"]:
                    if n < MAX_POTIONS:
                        self.potions.append(newPotion)
                        print(f'Has guardado la poción "{newPotion.name} {newPotion.emoji}"')
                    else:
                        print("No tienes espacio para guardar más pociones, debes elegir una para reemplazar")

                        for i in range(n):
                            potion = self.potions[i]
                            print(f'{i + 1}. {potion.name} {potion.emoji} ({potion.description})')
                        
                        while True:
                            position = self.askToPlayer("¿Qué poción quieres reemplazar? (ENTER para cancelar)")

                            if position in SPECIAL_COMMANDS: self.executeCommand(position)
                            else:
                                if position in availablePositions:
                                    oldPotion = self.potions[int(position) - 1]
                                    self.potions[int(position) - 1] = newPotion
                                    self.printWithTime(f'Has reemplazado la poción "{oldPotion.name} {oldPotion.emoji}" por "{newPotion.name} {newPotion.emoji}"')
                                else: self.printWithTime("Dejas la poción en el suelo")
                                return
                else:
                    self.printWithTime("Dejas la poción en el suelo")
                return


    # Muestra la pantalla de cuando el jugador es atacado
    def battle(self):
        enemyWeapon = choice(weapons)
        myWeapon = self.weaponInHand
        direction = choice(["left", "right"])

        print(f'Alguien te va a atacar con {enemyWeapon.usedName} {enemyWeapon.emoji}')
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

                if self.wonnedBattles == BATTLES_WON_BEFORE_FINAL_BATTLE: return self.finalBattle()
                return


    # Muestra la pantalla de cuando el jugador esta en la batalla final
    def finalBattle(self):
        sound.playFinalBattleMusic()
        self.printWithTime("Por fin has llegado al castillo de la montaña del oriente")
        self.printWithTime("De repente una voz detrás de ti te sobresalta:")
        self.printWithTime("")
        self.printWithTime(" - Te he estado esperando, estaba seguro que llegarías hasta aquí")
        self.printWithTime(" - Ella te dio y te dijo lo necesario para volver a tu mundo")
        self.printWithTime(" - Pero por supuesto, nunca te dijo quién te esperaría aquí")
        self.printWithTime(" - Apuesto a que ni siquiera sabes quién es ella")
        self.printWithTime(" - Apuesto a que ni siquiera sabes quién eres")
        self.printWithTime(" - Pero no te preocupes, eso ya no importa")
        self.printWithTime(" - No permitiré que llegues a la corona")
        self.printWithTime("")
        self.printWithTime("Tu enemigo saca su mejor arma y te ataca")

        while True:
            option = self.askToPlayer("Presiona ENTER para atacar")

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
                    self.printWithTime("Caes al suelo, no puedes más")
                    self.printWithTime("Tu enemigo te observa con una sonrisa y dice:")
                    self.printWithTime(" - Aún no eres digno, pero no te preocupes, volverás aquí")
                    self.printWithTime("Te despiertas en tu cama, todo ha sido un sueño")
                    self.__init__()
                    self.menuScreen()
                return

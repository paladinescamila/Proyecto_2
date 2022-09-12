import random
from Weapon import *
from Potion import *

# Posibles armas
weapons = [
    Weapon("🏹", "arco", 20), 
    Weapon("🔪", "daga", 30), 
    Weapon("🔨", "mazo", 40), 
    Weapon("🏹", "ballesta", 50), 
    Weapon("🗡️", "espada", 70)
]

# Posibles pociones
potions = [
    Potion("rehabilitar", 0),
    Potion("debilitar", 0),
    Potion("vida", 0)
]

# CLASE PLAYER

# Atributos
# - lifes
#   - Número de vidas (int)
#   - Inicia con 3 y no tiene límite
#   - Si llega a 0 pierde el juego
# - points:
#   - Número de puntos (int)
#   - Inicia con 200 y no tiene límite
#   - Si llega a 0 pierde una vida
#   - Si llega a 100 gana una vida
# - weapons
#   - Armas del jugador (lista de objetos Weapon)
#   - Inicia con 1 arma aleatoria
#   - Puede tener hasta 2 armas
#   - Al ganar una batalla puede tomar el arma del enemigo
# - potions
#   - Pociones del jugador (lista de objetos Potion)
#   - Inicia con 1 pocion aleatoria
#   - Puede tener hasta 50 pociones
#   - Las puede conseguir en cualquier parte del juego
# - wonnedBattles
#   - Número de batallas ganadas (int)
#   - Inicia con 0 y no tiene límite
#   - Al llegar a 10 batallas ganadas puede pelear por la corona

class Player:

    def __init__(self):
        self.lifes = 3
        self.points = 200
        self.weapons = [random.choice(weapons)]
        self.potions = [random.choice(potions)]
        self.wonnedBattles = 0
    

    def updateLifes(self, lifes):
        if (self.lifes + lifes > 0):
            if (lifes > 0):
                print("Has ganado una vida")
            else:
                print("Has perdido una vida")

            self.lifes += lifes

        else:
            print("Te has quedado sin vidas, perdiste el juego")


    def updatePoints(self, points):
        if (self.points + points > 0 and self.points + points < 100):
            if (points > 0):
                print(f'Has ganado {points} puntos')
            else:
                print(f'Has perdido {points * -1} puntos')

            self.points += points

        elif (self.points + points < 0):
            self.updateLifes(-1)
        else:
            self.updateLifes(1)


    def attack(self):
        weaponOrPotion = input("¿Quieres usar un arma o una poción? (A/p): ")

        if (weaponOrPotion == "p"):
            potionPosition = -1

            for i in range(len(self.potions)):
                if (self.potions[i].name == "debilitar"):
                    potionPosition = i
                    break
            
            if (potionPosition != -1):
                self.usePotion()
            else:
                print("No tienes pociones para debilitar")

        else:
            if (len(self.weapons) == 2):
                weaponPosition = input("¿Qué arma quieres usar? (1 ó 2, por defecto 1): ")

                if (weaponPosition == 2):
                    weapon = self.weapons[1]
                else:
                    weapon = self.weapons[0]

            else:
                weapon = self.weapons[0]

            print(f'Usando el arma {weapon.name}')
            print("Atacando")
        
        return weapon


    def beAttacked(self):
        enemyWeapon = random.choice(weapons)
        print(f'El enemigo te ha atacado con el arma {enemyWeapon.name}')

        myWeapon = self.attack()

        if (enemyWeapon.damage > myWeapon.damage):
            win = False
        elif (enemyWeapon.damage < myWeapon.damage):
            win = True
        else:
            win = random.choice([True, False])

        if (win):
            print("Has ganado esta batalla")
            saveWeapon = input("¿Quieres guardar la arma? (s/N): ")

            if (saveWeapon == "s"):
                self.saveWeapon(enemyWeapon)            

            self.wonnedBattles += 1

        else:
            print("Has perdido esta batalla")
            self.updatePoints(-enemyWeapon.damage)

        if (self.wonnedBattles == 10):
                goToTheCrown = input("¿Quieres ir por la corona? (S/n): ")

                if (goToTheCrown == "n"):
                    self.beAttacked()
                else:
                    self.fightForTheCrown()


    def fightForTheCrown(self):
        print("Peleando por la corona...")

        if (len(self.weapons) == 2):
            weaponPosition = input("¿Qué arma quieres usar? (1 ó 2, por defecto 1): ")

            if (weaponPosition == 2):
                weapon = self.weapons[1]
            else:
                weapon = self.weapons[0]

        else:
            weapon = self.weapons[0]

        print(f'Usando el arma {weapon.name}')
        print("Atacando...")

        win = random.choice([True, False])

        if (win):
            print("Has ganado el juego")
        else:
            print("Has perdido el juego")


    def saveWeapon(self, weapon):
        if (len(self.weapons) < 2):
            self.weapons.append(weapon)
        else:
            print("Tienes 2 armas, debes elegir cuál quieres reemplazar")

            for i in range(len(self.weapons)):
                print(f' {i + 1} - {self.weapons[i].name}')

            print("¿En qué posición quieres guardar la nueva arma?")
            newPosition = input("Elige 1, 2 ó 'X' (por defecto, si no quieres guardarla): ")

            if (newPosition == 1 or newPosition == 2):
                print(f'Has guardado el arma {weapon.name}')
                self.weapons[newPosition - 1] = weapon
        
        print("Ahora tienes las siguientes armas:")

        for i in range(len(self.weapons)):
            weapon = self.weapons[i]
            print(f' [{i + 1}] {weapon.emoji} {weapon.name} (daño: {weapon.damage})')
    

    def savePotion(self, potion):
        print(f'Guardando la pocion {potion.name}')
        self.potions.append(potion)


    def usePotion(self, potion):
        print(f'Usando la pocion {potion.name}')

        if (potion == "debilitar"):
            print("Has ganado la batalla")
            self.wonnedBattles += 1

        elif (potion == "rehabilitar"):
            self.updatePoints(50)

        elif (potion == "vida"):
            self.updateLifes(1)
        
        self.potions.remove(potion)


    def printState(self):
        print("--------------------")

        print("❤️ ", "Vidas:", self.lifes)
        print("⭐", "Puntos:", self.points)
        print("⚔️ ", "Partidas ganadas:", self.wonnedBattles)

        print("🗡️ Armas", f'({len(self.weapons)}/2):')
        for i in range(len(self.weapons)):
            weapon = self.weapons[i]
            print(f' [{i + 1}] {weapon.emoji} {weapon.name} (daño: {weapon.damage})')
        
        print("🧪 Pociones:")
        for i in range(len(self.potions)):
            potion = self.potions[i]
            print(f' [{i + 1}] {potion.name}')

        print("--------------------")
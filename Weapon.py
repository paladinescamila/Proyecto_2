class Weapon:
  
    def __init__(self, name, damage, emoji, usedName):
        self.name = name
        self.damage = damage
        self.emoji = emoji
        self.usedName = usedName

weapons = [
    Weapon("Arco", 20, "🏹", "un arco"),
    Weapon("Daga", 30, "🔪", "una daga"),
    Weapon("Mazo", 40, "🔨", "un mazo"),
    Weapon("Ballesta", 50, "🏹", "una ballesta"),
    Weapon("Espada", 70, "🗡️ ", "una espada"),
]

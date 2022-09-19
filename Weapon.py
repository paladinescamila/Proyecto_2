class Weapon:
  
    def __init__(self, name, damage, emoji, usedName):
        self.name = name
        self.damage = damage
        self.emoji = emoji
        self.usedName = usedName


weapons = [
    Weapon("Daga", 20, "🔪", "una daga"),
    Weapon("Hacha", 30, "🪓", "una hacha"),
    Weapon("Mazo", 40, "🔨", "un mazo"),
    Weapon("Ballesta", 50, "🏹", "una ballesta"),
    Weapon("Espada", 70, "🗡️ ", "una espada"),
]

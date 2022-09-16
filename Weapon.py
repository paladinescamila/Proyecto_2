class Weapon:
  
    def __init__(self, emoji, name, damage):
      self.emoji = emoji
      self.name = name
      self.damage = damage

weapons = [
    Weapon("🏹", "arco", 20),
    Weapon("🔪", "daga", 30),
    Weapon("🔨", "mazo", 40),
    Weapon("🏹", "ballesta", 50),
    Weapon("🗡️ ", "espada", 70)
]

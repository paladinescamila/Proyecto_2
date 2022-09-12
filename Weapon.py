# CLASE WEAPON

# Atributos
#   - name
#     - Nombre del arma (string)
#     - Posibles valores: arco, daga, mazo, ballesta, espada.
#   - damage
#     - Puntos que gana o pierde el jugador al usar el arma o ser atacado (int)
#     - Posibles valores: 20, 30, 40, 50 ó 70, según el arma. Puede ser positivo o negativo.

class Weapon:
  
    def __init__(self, emoji, name, damage):
      self.emoji = emoji
      self.name = name
      self.damage = damage
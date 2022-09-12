# CLASE POTION

# Atributos
#   - name
#     - Nombre de la pocion (string)
#     - Posibles valores: rehabilitar, debilitar, vida.
#  - effect
#     - Dependiendo de la pocion puede usarla con diferentes efectos
#     - Posibles valores: 
#       - rehabilitar: 50 puntos para el jugador
#       - debilitar: gana automáticamente el jugador
#       - vida: +1 vida para el jugador

class Potion:
  
  def __init__(self, name, effect):
    self.name = name
    self.effect = effect
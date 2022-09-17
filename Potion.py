class Potion:

    def __init__(self, name, description, message, value):
        self.name = name
        self.description = description
        self.message = message
        self.value = value

potions = [
    Potion("Fenix", "Obtienes una vida", "Has renacido de las cenizas.", 1),
    Potion("Poder", "Ganas 330 puntos", "Se te ha otorgado el poder de los dioses.", 300),
    Potion("Suerte de los dioses", "Ganas 200 puntos", "Los dioses te han bendecido.", 200),
    Potion("Oportunidad", "Ganas 100 puntos", "Aprovechaste la oportunidad.", 100)
]
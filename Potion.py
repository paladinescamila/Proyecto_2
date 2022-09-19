class Potion:

    def __init__(self, name, description, message, value, emoji):
        self.name = name
        self.description = description
        self.message = message
        self.value = value
        self.emoji = emoji


potions = [
    Potion("Fenix", "Si la bebes, ganas una vida", "Has renacido de las cenizas.", 1, "🐦"),
    Potion("Poder", "Si la bebes, ganas 300 puntos", "Se te ha otorgado el poder de los dioses.", 300, "🔥"),
    Potion("Suerte", "Si la bebes, ganas 200 puntos", "Los dioses te han bendecido.", 200, "🍀"),
    Potion("Oportunidad", "Si la bebes, ganas 100 puntos", "Aprovechaste la oportunidad.", 100, "🌟"),
]
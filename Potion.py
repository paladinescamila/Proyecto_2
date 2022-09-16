class Potion:

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

potions = [
    Potion("Fenix", "Has renacido de las cenizas.", 1),
    Potion("Poder", "Se te ha otorgado el poder de los dioses.", 300),
    Potion("Suerte de los dioses", "Los dioses te han bendecido.", 200),
    Potion("Oportunidad", "Aprovechaste la oportunidad.", 100)
]
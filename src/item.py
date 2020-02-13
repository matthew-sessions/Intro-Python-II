

class Item:
    def __init__(self, name, description):
        if ' ' in name:
            name = name.replace(' ', '_')
        self.name = name
        self.description = description
        self.on_drop = f"You droped the {name}"
        self.on_take = f"You picked up the {name}"
    def __str__(self):
        return(f"Item: {self.name}, - {self.description}")
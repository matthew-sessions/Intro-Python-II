

class Item:
    def __init__(self, name, description):
        if ' ' in name:
            name = name.replace(' ', '_')
        self.name = name
        self.description = description
    def __str__(self):
        return(f"Item: {self.name}, - {self.description}")
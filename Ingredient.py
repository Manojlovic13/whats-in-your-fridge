class Ingredient:
    def __init__(self, name, id, category = "none", needed = "none", image = "none"):
        self.name = name
        self.id = id
        self.category = category
        self.needed = needed
        self.image = image



    def __str__(self):
        return "ID:{id} NAME:{name}".format(self.id,self.name)
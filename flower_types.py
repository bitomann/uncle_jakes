class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.supply = 100

class IValentineFlower:
    def __init__(self):
        self.theme = "Love"
        

# class IOrganic:
#     def __init__(self):
#         self.organic = True
#         self.stem_length = 4
    
#     def transport_flowers(self, name):
#         print(f"The {name} were transported in a non-refrigerated case")
    

class INotOrganic:
    def __init__(self):
        self.organic =False
        self.stem_length = 7

    def transport_flowers(self, name):
        print(f"The {name} were transported in a refrigerated case")

class Rose(Flower, IValentineFlower):
    def __init__(self, color, length, container):
        Flower.__init__(self, length, container)
        IValentineFlower.__init__(self)
        self.color = color
        self.stem_length = 7
        self.container = "refrigerated"

class Daisies(Flower):
    def __init__(self, length, container):
        Flower.__init__(self, length, container)
        self.stem_length = 4
        self.container = "non-refrigerated"

class Baby_breath(Flower):
    def __init__(self, length, container):
        Flower.__init__(self, length, container)
        self.stem_length = 4
        self.container = "non-refrigerated"

class Poppies(Flower):
    def __init__(self, length, container):
        Flower.__init__(self, length, container)
        self.stem_length = "4 Inches"
        self.container = "non-refrigerated"

class Lilies(Flower):
    def __init__(self, length, container):
        Flower.__init__(self, length, container)
        IValentineFlower.__init__(self)
        self.stem_length = 7
        self.container = "refrigerated"
class Alstroemeria(Flower):
    def __init__(self, length, container):
        Flower.__init__(self, length, container)
        IValentineFlower.__init__(self)
        self.stem_length = 7
        self.container = "refrigerated"
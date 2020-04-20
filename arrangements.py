from flower_types import Flower

class Arrangement(Flower):

    def __init__(self):
        self.__flowers = []

    def enhance(self, flower):
        if flower.supply >=10:
            self.__flowers.append(flower)
            print(f"The {flower.name} were added to the arrangement!")
            flower.supply-= 10

        else:
            print(f"I am sorry but the {flower.name} are in short supply and we don't have enough to add this to the current arrangement")
    
    @property
    def flowers(self):
        return self.__flowers
    
    @flowers.setter
    def flowers(self, flower):
            self.__flowers.append(flower)
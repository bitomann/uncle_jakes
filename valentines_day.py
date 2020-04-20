from arrangements import Arrangement

class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        if flower.supply >=10:
            if flower.name == "Roses" or "Lilies" or "Alstroemeria":
                self.flowers = flower
                print(f"The {flower.name} were added to the arrangement!")
                flower.supply-= 10
            else:
                print(f"I am sorry, but {flower.name} aren't allowed in the Mother's Day arrangement.")
        else:
            print(f"I am sorry but the {flower.name} are in short supply and we don't have enough to add this to the current arrangement")
# Your task is to define classes for each type of flower, 
# and a class for each arrangement type. Each arrangement 
# instance should have an attribute of flowers which will 
# contain at least one of each type of the corresponding 
# flowers listed above.

# Your code must ensure that only the right flowers can be 
# added to each arrangement.

# Rose, lilies, and alstroemeria share some attribute that 
# the others do not (perfect case for an interface class)

# All flowers share some common attributes

from valentines_day import ValentinesDay
from flower_types import Baby_breath, Daisies, Lilies, Poppies, Rose, Alstroemeria
from mothers_day import MothersDay
from arrangements import Arrangement

if __name__ == "__main__":

    for_beth = ValentinesDay()
    red_roses = Rose("Red", 7, "refrigerated")
    
    Daisies("Yellow", "non-refrigerated")
    Poppies("Red", "non-refrigerated")
    Baby_breath('White', "non-refrigerated")
    Lilies("Pink", "refrigerated")
    Alstroemeria("Yellow", "refrigerated")

    for_mom = MothersDay()
    # print(red_roses.name, daisies.name, poppies.stem_length, lilies.color, alstroemerias.organic)
    # babies.transport_flowers(babies.name)
    # lilies.transport_flowers(lilies.name)

    for_beth.enhance(red_roses)
    for_beth.enhance(Lilies)
    for_beth.enhance(Alstroemeria)
    for_mom.enhance(Daisies)
    for_mom.enhance(Poppies)
    for_mom.enhance(Baby_breath)
    for_mom.enhance(red_roses)

    # print (red_roses.supply)
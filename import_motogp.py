# Importing Multiple Classes

# This could be rewritten 'from motogp_oop import *'
# Listing out the classes and or modules being imported is recommended
# It helps to avoid errors 
# and is easy to determine which classes and or modules were imported in

from motogp_oop import Sports_Motorcycle, Motogp

# Creating instances from the classes these cover Ducati, Honda, and Yamaha 
# Both the the street legal and the Motogp racing bikes
duc = Sports_Motorcycle('Ducati', 'Panigale V4')
hon = Sports_Motorcycle('Honda', 'CBR 1000RR')
yam = Sports_Motorcycle('Yamaha', 'YZF R1')

mduc = Motogp('Ducati', 'Desmosedici')
mhon = Motogp('Honda', 'Repsol RC213V')
myam = Motogp('Yamaha', 'Movistar')

# beginning to access the attributes
print(
    "\nThe " + duc.description() + "and " + str(mduc.model) + " will be "
    "reviewed first.\n"
    )

print(
    "***** " + duc.description() + "*****"
    )
    
# Accessing Attributes and calling in imported methods
# The values differ from manufacturer & model
# As many instances as needed can be created
# I chose to utlize 6 motorcycles
duc.engine_size = 1103
duc.engine()
duc.dry_weight = 381
duc.weight()
duc.speed = 190
duc.top_speed()
duc.price = 40000
duc.msrp()

print(
    "\n***** " + mduc.description() + "*****"
    )
mduc.engine_size = 1000
mduc.engine()
mduc.dry_weight = 346.12
mduc.weight()
mduc.speed = 225
mduc.top_speed()
mduc.buy_racing_motorcycle()

print("\n***** Comparison of Performance (Speed & Weight) *****\n"
    )

# While loop utilized to compare the street sports bike vs motogp bike
while True:
    if duc.speed > mduc.speed and duc.dry_weight < mduc.dryweight:
        print(
            "The " + duc.description() + "is both faster at " + 
            str(duc.speed) + "mph, compared to " + str(mduc.speed) + 
            "mph, \nand lighter at " + str(duc.dry_weight) + " pounds, "
            "compared to " + str(mduc.dry_weight) + " pounds than the " + 
            str(mduc.model) + "."
            )
# else break statement prevents an infinite loop!  
    else:
        break
    
if duc.speed < mduc.speed and duc.dry_weight > mduc.dry_weight:
    print(
            "The " + mduc.description() + "is both faster at " + 
            str(mduc.speed) + "mph, compared to " + str(duc.speed) + 
            "mph, \nand lighter at " + str(mduc.dry_weight) + 
            "pounds, compared to " + str(duc.dry_weight) + 
            "pounds than the " + str(duc.model) + "."
            )
            
# The process repeats for Honda and Yamaha below
print(
    "\nThe " + hon.description() + "and " + str(mhon.model) + " will be "
    "reviewed next.\n"
    )

print(
    "***** " + hon.description() + "*****"
    )
    
hon.engine_size = 998.8
hon.engine()
hon.dry_weight = 390
hon.weight()
hon.speed = 186
hon.top_speed()
hon.price = 21200
hon.msrp()

print(
    "\n***** " + mhon.description() + "*****"
    )
mhon.engine_size = 1000
mhon.engine()
mhon.dry_weight = 346.12
mhon.weight()
mhon.speed = 220
mhon.top_speed()
mhon.buy_racing_motorcycle()

print("\n***** Comparison of Performance (Speed & Weight) *****\n"
    )

while True:
    if hon.speed > mhon.speed and hon.dry_weight < mhon.dryweight:
        print(
            "The " + hon.description() + "is both faster at " + 
            str(hon.speed) + "mph, compared to " + str(mhon.speed) + 
            "mph, \nand lighter at " + str(hon.dry_weight) + " pounds, "
            "compared to " + str(mhon.dry_weight) + " pounds than the " + 
            str(mhon.model) + "."
            )
    else:
        break
    
if hon.speed < mhon.speed and hon.dry_weight > mhon.dry_weight:
    print(
            "The " + mhon.description() + "is both faster at " + 
            str(mhon.speed) + "mph, compared to " + str(hon.speed) + 
            "mph, \nand lighter at " + str(mhon.dry_weight) + 
            "pounds, compared to " + str(hon.dry_weight) + "pounds than the " 
            + str(hon.model) + "."
            )
            
print(
    "\nThe " + yam.description() + "and " + str(myam.model) + " will be "
    "reviewed last.\n"
    )

print(
    "***** " + yam.description() + "*****"
    )
    
yam.engine_size = 998
yam.engine()
yam.dry_weight = 414
yam.weight()
yam.speed = 182
yam.top_speed()
yam.price = 17399
yam.msrp()

print(
    "\n***** " + myam.description() + "*****"
    )
myam.engine_size = 1000
myam.engine()
myam.dry_weight = 346.12
myam.weight()
myam.speed = 211
myam.top_speed()
myam.buy_racing_motorcycle()

print("\n***** Comparison of Performance (Speed & Weight) *****\n"
    )

while True:
    if yam.speed > myam.speed and yam.dry_weight < myam.dryweight:
        print(
            "The " + yam.description() + "is both faster at " + 
            str(yam.speed) + "mph, compared to " + str(myam.speed) + 
            "mph, \nand lighter at " + str(yam.dry_weight) + " pounds, "
            "compared to " + str(myam.dry_weight) + " pounds than the " + 
            str(myam.model) + "."
            )
    else:
        break
    
if yam.speed < myam.speed and yam.dry_weight > myam.dry_weight:
    print(
            "The " + myam.description() + "is both faster at " + 
            str(myam.speed) + "mph, compared to " + str(yam.speed) + 
            "mph, \nand lighter at " + str(myam.dry_weight) + 
            "pounds, compared to " + str(yam.dry_weight) + 
            "pounds than the " + str(yam.model) + "."
            )

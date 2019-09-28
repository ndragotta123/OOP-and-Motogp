# Object Oriented Program for motogp

# Building Parent Class of Sports Motorcycle
class Sports_Motorcycle():
    """Model Street Legal Sports Motorcycle"""

# Create init Method for parameters self, manufacturer, model of motorycle
# Added attributes with value 0 for later use
    def __init__(self, manufacturer, model):
        """Build manufacturer and model of sports bike"""
        self.manufacturer = manufacturer
        self.model = model
        self.engine_size = 0
        self.dry_weight = 0
        self.speed = 0
        self.price = 0

# Create method to describe attributes of motorcyle
    def description(self):
        """Description of each Motorcyle"""
        desc = self.manufacturer + ' ' + str(self.model) + ' '
        return desc

# Create method that is easy to determine engine size of motorcycle    
    def engine(self):
        """Engine size of each Motorcyle"""
        print(
            "This motorcycle has a " + str(self.engine_size) + "cc engine."
            )

# Create method that is easy to determine weight of motorcycle
    def weight(self):
        """Dry weight of Sports Motorcycle"""
        print(
            "With a dry weight of " + str(self.dry_weight) + " pounds."
            )
            
# Create method that is easy to determine top speed of motorcycle
    def top_speed(self):
        """Top Speed of Sports Motorcycle"""
        print(
            "The top speed for the " + str(self.model) + " is " 
            + str(self.speed) + "mph."
            )

# Create method that is easy to determine MSRP of motorcycle
    def msrp(self):
        """Retail Price of Sports Motorcycle"""
        print(
            "The sales price is $" + str(self.price) + " USD."
            )

# Create Child class for Motogp Motorcycle (inherits all traits of parent)
class Motogp(Sports_Motorcycle):
    """Model Motogp version of the Sports Motorcycle"""

# Setup init method to inherit the traits of parent class Sports_Motorcycle
    def __init__(self, manufacturer, model):
        """Build manufacturer and model of sports bike"""
        super().__init__(manufacturer, model)

# Create method to override parent class MSRP as racing bikes cant be bought
    def buy_racing_motorcycle(self):
        """Unable to buy a Motogp motorcycle"""
        print(
            "Motogp Motorcycles are not for sale"
            )

# [x] To the GroundVehicle class, add method drive() that returns "vroooom".
#
# [x] Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle:
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    @staticmethod
    def drive():
        return "vroooom"


# [x] Subclass Motorcycle from GroundVehicle.
#
# [x] Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# [x] Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self):
        """ Defaults the motorcycle to two wheels """
        super().__init__(2)

    @staticmethod
    def drive():
        return "BRAAAP!!"


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# [x] Go through the vehicles list and print the result of calling drive() on each.

for vehicle in vehicles:
    print(vehicle.drive())


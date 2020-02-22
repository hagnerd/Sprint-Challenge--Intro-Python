# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# The base class is going to be Vehicle

class Vehicle:
    """ The base class for all other types of vehicles """
    pass


class GroundVehicle(Vehicle):
    """ A category of vehicle focused on traveling via the ground """
    pass


class Car(GroundVehicle):
    """ A specific ground vehicle that has four wheels """
    pass


class Motorcycle(GroundVehicle):
    """ A specific ground vehicle that has two wheels """
    pass


class FlightVehicle(Vehicle):
    """ A category of vehicle focused on air travel within the stratoshpere """
    pass


class Airplane(FlightVehicle):
    """ A specifc flight vehicle """
    pass

class Starship(FlightVehicle):
    """ A category of vehicle focused on travel through space, extends
    FlightVehicle """
    pass


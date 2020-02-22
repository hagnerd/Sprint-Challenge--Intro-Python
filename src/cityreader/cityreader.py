# [x] Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lon}"



# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# [x] In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

import csv
import textwrap

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the
  # `cities` list
    with open('cities.csv') as citiesfile:
        cities_csv = csv.DictReader(citiesfile, delimiter=',')
        for row in cities_csv:
            cities.append(City(row['city'], float(row['lat']),
                               float(row['lng'])))
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def does_coord_fall_between(lat_or_lon, l1, l2):
    maximum = max([l1, l2])
    minimum = min([l1, l2])
    return minimum <= lat_or_lon <= maximum

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []
    lat1 = float(lat1)
    lat2 = float(lat2)
    lon1 = float(lon1)
    lon2 = float(lon2)

    for city in cities:
        if does_coord_fall_between(city.lat, lat1, lat2) and does_coord_fall_between(city.lon, lon1, lon2):
            within.append(city)
    return within


def get_lat_lon_pair(message):
    lat_lon = input(message)
    lat_lon = lat_lon.split(',')
    if len(lat_lon) != 2:
        print('Inavlid input\n')
        get_lat_lon_pair(message)
    else:
        return (float(lat_lon[0]), float(lat_lon[1]))

def inital_instructions():
    print('\n'.join(textwrap.wrap("""We will ask you for two latitude and longitude pairs and return a
list of all cities that with populations over 750,000 that fall within those
                        longitudes and lattitudes""", 80)))

def main():
    global cities
    inital_instructions()
    lat1, lon1 = get_lat_lon_pair('Enter the first latitude and longitude pair separated by a comma: \n')
    lat2, lon2 = get_lat_lon_pair('Enter the second latitude and longitude pair separated by a comma: \n')
    print(f"Finding all cities between {lat1}, {lon1} and {lat2}, {lon2}")
    for city in cityreader_stretch(lat1, lon1, lat2, lon2, cities):
        print(city)

main()

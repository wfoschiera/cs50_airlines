# import os

# os.system("python manage.py shell")
from flights.models import *

airports_to_fill = {'JFK':'New York', 'LHR': 'London', 'CDG': 'Paris', 'NRT': 'Tokyo'}
airports_objects = {}

for code_, city_ in airports_to_fill.items():
    new_airport = Airport(code=code_, city=city_)
    new_airport.save()
    airports_objects[new_airport.code] = new_airport

flights = {1: (airports_objects['JFK'], airports_objects['LHR'], 315),
           2: (airports_objects['JFK'], airports_objects['CDG'], 435)}

for key, new_flight in flights.items():
    flight = Flight(origin=new_flight[0], destination=new_flight[1], duration=new_flight[2])
    flight.save()

# Obs: Se eu já possuir os registros dos aeroportos, posso construir os objetos através de consultas
# e utilizá-los para criar novos voôs. P.e.: 
# jfk = Airport.objects.get(city="New York")
# cdg = Airport.objects.get(city="Paris")
# f = Flight(origin=jfk, destination=cdg, duration=435)
destinations = ['paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

#Testing the test Traveler to mak sure basic functionality is there
#print(get_traveler_location(test_traveler))

attractions = [[] for i in destinations]

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(attraction)

    except SyntaxError:
        return


add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction('Paris, France', ['the Louvre', ['art', 'museum']])
add_attraction('Paris, France', ['Arc de Triomphe', ['historical site', 'monument']])
add_attraction('Shanghai, China', ['Yu Garden', ['garden', 'historical site']])
add_attraction('Shanghai, China', ['Yuz Museum', ['art', 'museum']])
add_attraction('Shanghai, China', ['Oriental Pearl Tower', ['skyscrapper', 'viewing deck']])
add_attraction('Los Angeles, USA', ['LACMA', ['art', 'museum']])
add_attraction('Sao Paulo, Brazil', ['Sao Paulo Zoo', ['zoo']])
add_attraction('Sao Paulo, Brazil', ['Patio do Colegio', ['historical site']])
add_attraction('Cairo, Egypt', ['Pyramids of Giza', ['monument', 'historical site']])
add_attraction('Cairo, Egypt', ['Egyption Museum', ['museum']])

print(attractions)

destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    dest_index = destinations.index(destination)
    return dest_index


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    trav_dest_index = get_destination_index(traveler_destination)
    return trav_dest_index


test_dest_index = get_traveler_location(test_traveler)


print(test_dest_index)

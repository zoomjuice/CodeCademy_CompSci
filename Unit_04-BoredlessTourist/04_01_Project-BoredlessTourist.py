"""
TODO:
    -Refactor this garbage into classes
"""

destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']
attractions = [[] for dest in destinations]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    dest_index = destinations.index(destination)
    return dest_index


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    trav_dest_index = get_destination_index(traveler_destination)
    return trav_dest_index


def add_attraction(destination, attraction):
    try:
        dest_index = get_destination_index(destination)
    except ValueError:
        return
    attractions[dest_index].append(attraction)
    return


def find_attractions(destination, interests):
    dest_index = get_destination_index(destination)
    attractions_in_city = attractions[dest_index]
    attractions_with_interest = []
    for att in attractions_in_city:
        for interest in interests:
            if interest in att[1] and att not in attractions_with_interest:
                attractions_with_interest.append(att[0])
    return attractions_with_interest


def get_attractions_for_traveler(traveler):
    name = traveler[0]
    dest = traveler[1]
    interests = traveler[2]
    traveler_attractions = find_attractions(dest, interests)
    interests_message = "Hi {n}, we think you'll like these places around {dest}: ".format(n=name, dest=dest)
    for att in traveler_attractions:
        interests_message += '\n' + str(att)
    return interests_message


add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

la_arts = find_attractions('Los Angeles, USA', ['art'])
testvar = find_attractions(test_traveler[1], test_traveler[2])

print(get_attractions_for_traveler(test_traveler))

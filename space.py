import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('name')
            mass = planet.get('mass').get('massValue')
            orbit_period = planet.get('sideralOrbit')
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    return planets

def find_heaviest_planet(planets):
    planets_mass = []
    for planet in planets:
        if planet['isPlanet']:
            mass = planet.get('mass').get('massValue')
            name = planet.get('name')
            planets_mass.append({'name': name, 'mass': mass})
    return max(planets_mass, key=lambda planet: planet.get("mass"))

planets = fetch_planet_data()
heaviest_planet = find_heaviest_planet(planets)
print(f"The heaviest planet is {heaviest_planet.get('name')} with a mass of {heaviest_planet.get('mass')} kg.")

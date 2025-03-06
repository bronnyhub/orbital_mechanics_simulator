import numpy as np
import matplotlib.pyplot as plt

PLANETS = {
    "Mercury": {"mass": 3.3011e23, "radius": 2439.7e3},
    "Venus": {"mass": 4.8675e24, "radius": 6051.8e3},
    "Earth": {"mass": 5.972e24, "radius": 6371e3},
    "Mars": {"mass": 6.4171e23, "radius": 3389.5e3},
    "Jupiter": {"mass": 1.898e27, "radius": 69911e3},
    "Saturn": {"mass": 5.683e26, "radius": 58232e3},
    "Uranus": {"mass": 8.681e25, "radius": 25362e3},
    "Neptune": {"mass": 1.024e26, "radius": 24622e3}
}

planet_name = input("Choose a planet (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune): ")

planet = PLANETS.get(planet_name, PLANETS["Earth"])
M_planet = planet["mass"]
R_planet = planet["radius"]

print(f"Simulating orbit around {planet_name} (Mass: {M_planet} kg, Radius: {R_planet} m)")
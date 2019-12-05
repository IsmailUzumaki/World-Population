from pygal_maps_world.maps import World
import json
from countrycodes import *
from pygal.style import RotateStyle

filename = 'population_data.json'


with open(filename) as f:
    pop_data = json.load(f)
# Build a dictionary of population data
    cc_population = {}
    # Print the data for population in 2010
    for pop_dict in pop_data:
        if pop_dict['Year'] == "2010":
            country = pop_dict['Country Name']
            country_code = pop_dict['Country Code']
            population = float(pop_dict['Value'])
            code = get_country_code(country)
            if code:
                cc_population[code] = population

    # Group the countries into 3 population levelss.
    cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
    for cc, pop in cc_population.items():
        if pop < 10000000:
            cc_pop_1[cc] = pop
        elif pop < 1000000000:
            cc_pop_2[cc] = pop
        else:
            cc_pop_3[cc] = pop
        # How manny countries in each level
    print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))
    world_map_style = RotateStyle('#336699')
    world_map = World(style=world_map_style)
    world_map.title = 'World Population in 2010, by country'

    world_map.add('0-10m ', cc_pop_1)
    world_map.add('10m-1bn ', cc_pop_2)
    world_map.add('>1bn ', cc_pop_3)

    world_map.render_to_file('world_populations.svg')







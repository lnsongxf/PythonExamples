#==============================================================================
# purpose: implementation of k-NN classification as in Chapter 3 of Kirk (2015)
# author: tirthankar chakravarty
# created: 27/6/15
# revised: 
# comments:
# This script makes use of collections.namedtuple to create the neighbour house "struct"
# Then the neighbour houses are sorted by the distance to each prospective house.
==============================================================================

import numpy as np
import numpy.linalg as npl
from collections import OrderedDict, namedtuple

neighbours = {(56, 2): 1, (3, 20): 0, (18, 1): 1, (20, 14): 0, (30, 30): 1, (35, 35): 1}
house1 = (10, 10)
house2 = (40, 40)

# compute the distance of the houses from the neighbours and keep the top 3
def get_nn(*args, neighbours, k=3):
    """ Return a dictionary with nearest neighbour probabilities (sorted)
    :param args: tuples with the locations of houses that need to be classified
    :param neighbours: dictionary with the location and happiness of the neighbours
    :return: dictionary with key as location of prospective house,
        and value as the classification probability of being a happy house
    """
    # namedtuple representing each neighbour
    NeighbourHouse = namedtuple("NeighbourHouse", ["HouseLocation", "Distance", "Happiness"])
    # compute the distance of each prospective house from the neighbours
    houses_neighbours = {prospective_house: [NeighbourHouse(HouseLocation=neighbour_location,
                                                         Distance=npl.norm(np.array(prospective_house) -
                                                                           np.array(neighbour_location)),
                                                         Happiness=neighbour_happiness)
                                          for neighbour_location, neighbour_happiness in neighbours.items()]
                         for prospective_house in args}
    # sort the nieghbours by distance from each prospective house
    houses_neighbours_sorted = {prospective_house: sorted(houses_neighbours[prospective_house],
                                                       key=lambda NeighbourHouse: NeighbourHouse.Distance)
                                for prospective_house in houses_neighbours.keys()}
    # get the happiness of each of the neighbours of prospective houses
    houses_neighbours_sorted_happiness = \
        {prospective_house: [getattr(house_n, "Happiness") for house_n in
                          houses_neighbours_sorted[prospective_house]]
         for prospective_house in houses_neighbours_sorted.keys()}
    # compute the likely happiness of each of the prospective houses as the average happiness of
    #   the first k nearest neighbours
    avg_dist_houses = {prospective_house: np.average(houses_neighbours_sorted_happiness[prospective_house][0:k])
                       for prospective_house in houses_neighbours_sorted_happiness}
    return(avg_dist_houses)

dist_houses = get_nn(house1, house2, neighbours=neighbours)

# Conclusion: The chances that you are going to be happy, given the happiness of the neighbours,
#   are higher if you pick the prospective house at (10, 10) rather than the house at (40, 40)

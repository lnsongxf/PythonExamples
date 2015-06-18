# ==============================================================================
# purpose: create statistical distribution objects, and find shortest paths
# author:
# created: 6/6/15
# revised: 
# comments:
# 1. This is based on the object graph on Wikipedia.
# 2. The idea is to create a graph of the various continuous statistical distributions,
#   plot them, and traverse the graph to find the shortest distance paths.
# 3. Could use the Python module objgraph to do this, where the nodes are the distributions
#   but inheritance is the only relationship here, so cannot have the relationships that we need
#   such as deterministic relationships, and approximate relationships.
# 4. How does an ontology fit into the picture.
#==============================================================================
import scipy.stats as sps
import math


class StatisticalDistribution(object):
    def __init__(self):
        pass

    def compute_percentile(self, percentile):
        pass


class NormalDistribution(StatisticalDistribution):
    def __init__(self, mean=0, var=1):
        self.mean = mean
        self.var = var

    def compute_percentile(self, percentile=0.5):
        rv = sps.norm(loc=self.mean, scale=math.sqrt(self.var))
        return rv.ppf(percentile)


class LogNormalDistribution(StatisticalDistribution):
    def __init__(self, mean=0, var=1):
        self.mean = mean
        self.var = var

    def compute_percentile(self, percentile=0.5):
        rv = sps.lognorm(s=math.sqrt(self.var), scale=math.exp(self.mean))
        return rv.ppf(percentile)


x = NormalDistribution(mean=3, var=4)
x.compute_percentile()

y = LogNormalDistribution(mean=3, var=4)
y.compute_percentile()




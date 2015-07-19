#==============================================================================
# purpose: bivariate normal distribution simulation using PyMC
# author: tirthankar chakravarty
# created: 1/7/15
# revised: 
# comments:
# 1. install PyMC
# 2. not clear on why we are helping the sampler along. We want to sample from the
#   bivariate
#==============================================================================

import random
import numpy as np
import matplotlib.pyplot as mpl

sample_size = 5e5
rhp = 0.9

mean = [10, 20]
std_dev = [1, 1]

biv_random = np.zeros([sample_size, 2])
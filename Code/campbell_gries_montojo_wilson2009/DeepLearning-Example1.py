#==============================================================================
# purpose: simple deep learning example
# author: tirthankar chakravarty
# created: 6th april 2015
# revised:
# comments:
# 1. this is based on the example here:
#   http://deeplearning.net/tutorial/gettingstarted.html#gettingstarted
#==============================================================================

import cPickle, gzip, numpy
f = gzip.open("Code/DeepLearning/Data/mnist.pkl.gz")                           # open a connection to the data
train_set, valid_set, test_set = cPickle.load(f)
f.close()

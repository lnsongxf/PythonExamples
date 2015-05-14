# ==============================================================================
# purpose: create a dict of Python DataFrames from a DataFrame
# author: tirthankar chakravarty
# created: 13/5/15
# revised: 
# comments:
#==============================================================================

import pandas as pd
import numpy.random as npr


dfM = pd.DataFrame({
    "group_var": npr.random_integers(low = 0, high = 10, size = 100),
    "data_var": npr.normal(size = 100)
})

dfMG = dict(list(dfM.groupby('group_var')))



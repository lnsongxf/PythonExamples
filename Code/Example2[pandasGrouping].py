#====================================================================
# purpose: fast grouping in pandas
# author: tirthankar chakravarty
# created: 20th january 2015
# revised:
# comments: Based on Matt Dowle's example on SO:
#     http://stackoverflow.com/questions/25631076/is-this-the-fastest-way-to-group-in-pandas
#====================================================================

import pandas as pd
import numpy as np
import timeit
print(pd.__version__)

# function: returns random group identifiers
def randChar(f, numGrp, N):
   things = [f%x for x in range(numGrp)]
   return [things[x] for x in np.random.choice(numGrp, N)]

# function: returns random numbers
def randFloat(numGrp, N):
   things = [round(100*np.random.random(),4) for x in range(numGrp)]
   return [things[x] for x in np.random.choice(numGrp, N)]

N = int(1e4)
K = 100
DF = pd.DataFrame({
  'id1' : randChar("id%03d", K, N),       # large groups (char)
  'id2' : randChar("id%03d", K, N),       # large groups (char)
  'id3' : randChar("id%010d", N//K, N),   # small groups (char)
  'id4' : np.random.choice(K, N),         # large groups (int)
  'id5' : np.random.choice(K, N),         # large groups (int)
  'id6' : np.random.choice(N//K, N),      # small groups (int)
  'v1' :  np.random.choice(5, N),         # int in range [1,5]
  'v2' :  np.random.choice(5, N),         # int in range [1,5]
  'v3' :  randFloat(100,N)                # numeric e.g. 23.5749
})

#==========================================================
# time aggregation methods
#==========================================================
timeit.Timer("DF.groupby(['id1']).agg({'v1':'sum'})",
             "from __main__ import DF").timeit(1)

timeit.Timer("DF.groupby(['id1', 'id2']).agg({'v1':'sum'})",
             "from __main__ import DF").timeit(1)

timeit.Timer("DF.groupby(['id3']).agg({'v1':'sum', 'v3':'mean'})",
             "from __main__ import DF").timeit(1)

timeit.Timer("DF.groupby(['id4']).agg({'v1':'mean', 'v2':'mean', 'v3':'mean'})",
             "from __main__ import DF").timeit(1)

timeit.Timer("DF.groupby(['id6']).agg({'v1':'sum', 'v2':'sum', 'v3':'sum'})",
             "from __main__ import DF").timeit(1)

#==========================================================
# plot the aggregations
#==========================================================
dfAgg1 = DF.groupby(['id1']).agg({'v1':'sum'})
dfAgg1.plot()

dfAgg2 = DF.groupby(['id4']).agg({'v1':'mean', 'v2':'mean', 'v3':'mean'})
dfAgg2.plot()
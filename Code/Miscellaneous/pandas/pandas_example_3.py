# ==============================================================================
# purpose: follow along to the 10 minute tutorial on pandas:
#   http://pandas.pydata.org/pandas-docs/version/0.15.2/10min.html
# author: tirthankar chakravarty
# created: 12/4/15
# revised: 
# comments:
#==============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 2, 3, np.nan, np.nan, 7])
dates = pd.date_range("20130201", periods= 6)
df1 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns = list('ABCD'))  # creating DataFrame from np.matrix
df2 = pd.DataFrame({
    'A': 1.0,                                                                   # series are recycled
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})
df2.dtypes                                                                     # check the column types
df2.A
df2.head(3)
df2.tail(3)
df2.columns
df2.values

df1.describe()
df1.T
df1.sort(axis = 0, ascending = True)

df1['A']
df1.A
df1[0:1]
df1.loc[:, ['A', 'B']]
df1.loc[dates[0]]
df1.at[dates[0], 'A']

df1.iloc[3:5, 1:2]
df1.iat[2, 3]

df2[df2.A == 1.]

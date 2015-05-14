
# convert R data.frame to Python DataFrame
import pandas.rpy.common as com
infert = com.load_data('infert')
infert.head()

# convert Python DataFrame to an R data.frame
from pandas import DataFrame
df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C':[7,8,9]},
   index = ["one", "two", "three"])
r_dataframe = com.convert_to_r_dataframe(df)
print(type(r_dataframe))
print(r_dataframe)


#==============================================================================
# purpose: follow along to the pandas Burrito tutorial:
#   http://www.danielforsyth.me/pandas-burritos-analyzing-chipotle-order-data-2/
# author: tirthankar chakravarty
# date: 25th april 2015
#==============================================================================

import pandas as pd
import matplotlib.pyplot as mpl

dfC = pd.read_csv("Data/orders.tsv", sep='\t')
dfC.head()

# what are the most popular items?
items = dfC.item_name.value_counts().plot(kind='bar')
items = dfC.item_name.value_counts()[:10].plot(kind='bar')
mpl.show()

# what is the price of the items
dfC['item_price'] = dfC['item_price'].str.replace('$', '')
dfC['item_price'] = dfC['item_price'].astype('float')
orders = dfC.groupby('order_id').sum()
orders.head()

# check the most popular kinds of chicken bowl combinations
descriptions = dfC.groupby(['item_name', 'choice_description'])['order_id'].count().reset_index(name='count')
descriptions.head()

descriptions = descriptions[descriptions['item_name'].str.contains("Chicken Bowl")]
descriptions.sort(['count'], ascending=False)[:10]

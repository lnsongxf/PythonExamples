# ==============================================================================
# purpose: download and cluster Discogs monthly new record releases
# author: tirthankar chakravarty
# created: 3/6/15
# revised: 
# comments:
#==============================================================================

import functools
import os
import pandas as pd
from SensitiveInformation.discogs_application_info import provide_discogs_auth, provide_verifier
import discogs_client
import urllib as ul

# interact with the Discogs API
discogs_consumer_key, discogs_consumer_secret = provide_discogs_auth()
discogs = discogs_client.Client(user_agent="ThoughtfulMachineLearning",
                                consumer_key=discogs_consumer_key,
                          consumer_secret=discogs_consumer_secret)
# discogs_auth_url = discogs.get_authorize_url()
discogs.get_access_token(verifier=provide_verifier())

# get the first 50 pages of search results for Jazz records
discogs_query_jazz = discogs.search(genre="jazz")  # this returns a pagination object
df_discogs_releases = {pagenum: pd.DataFrame(
    (x.data for x in discogs_query_jazz.page(pagenum))) for pagenum in range(50)}
df_jazz_releases = functools.reduce(pd.DataFrame.append, df_discogs_releases.values())

# save the DataFrame as a CSV file
isinstance(df_jazz_releases, pd.DataFrame)
# df_jazz_releases.to_csv("Data/jazz_releases.csv")  # not very helpful

# create some new variables
series_jazz_thumbs = df_jazz_releases.thumb
isinstance(series_jazz_thumbs, pd.Series)

os.mkdir(path="Data/Discogs_Thumbnails")
[open('Data/Discogs_Thumbnails/Thumb %s.jpg' % index, 'wb').write(
    ul.request.urlopen(series_jazz_thumbs.iloc[index]).read()) for index in
 series_jazz_thumbs.index if not series_jazz_thumbs.iloc[index] == '']


#==============================================================================
# purpose: examples of Excel tasks with pandas
# author: tirthankar chakravarty
# created: 14/7/15
# revised: 
# comments: this is taken from the tutorial here:
#   http://pbpython.com/excel-pandas-comp.html
#==============================================================================

import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz, process
import numpy.random as npr

df_excel = pd.read_excel("Data/excel-comp-data.xlsx")
df_excel.head()

# task 1: create the total of a range of rows by name
df_excel["month_total"] = df_excel[["Jan", "Feb", "Mar"]].sum(axis=1)
df_excel["month_total2"] = df_excel[[6, 7, 8]].sum(axis=1)

# task 2: get the summary statistics of columns
df_excel["Jan"].mean(), df_excel["Jan"].sum(), df_excel["Jan"].min(), df_excel["Jan"].max()

# task 3: add a row which does not have all the columns in the data
df_newrow = pd.DataFrame(data = pd.Series({"Jan": 10000, "Feb": 20000, "Mar": 400000})).T
df_newrow = df_newrow.reindex(columns=df_excel.columns)
df_excel.append(df_newrow)

# task 4: install and run through the examples of the FuzzyWuzzy package
# task 5: create the abbreviation of a column basis a fuzzy lookup
# install python-Levenshtein to get a fast backend for the metric distance computation
# - ratio
# - partial ratio
# - token set ratio
# - token sort ratio
fuzz.ratio("This is a string.", "This is a different string.")
state_to_code = {"VERMONT": "VT", "GEORGIA": "GA", "IOWA": "IA", "Armed Forces Pacific": "AP", "GUAM": "GU",
                 "KANSAS": "KS", "FLORIDA": "FL", "AMERICAN SAMOA": "AS", "NORTH CAROLINA": "NC", "HAWAII": "HI",
                 "NEW YORK": "NY", "CALIFORNIA": "CA", "ALABAMA": "AL", "IDAHO": "ID", "FEDERATED STATES OF MICRONESIA": "FM",
                 "Armed Forces Americas": "AA", "DELAWARE": "DE", "ALASKA": "AK", "ILLINOIS": "IL",
                 "Armed Forces Africa": "AE", "SOUTH DAKOTA": "SD", "CONNECTICUT": "CT", "MONTANA": "MT", "MASSACHUSETTS": "MA",
                 "PUERTO RICO": "PR", "Armed Forces Canada": "AE", "NEW HAMPSHIRE": "NH", "MARYLAND": "MD", "NEW MEXICO": "NM",
                 "MISSISSIPPI": "MS", "TENNESSEE": "TN", "PALAU": "PW", "COLORADO": "CO", "Armed Forces Middle East": "AE",
                 "NEW JERSEY": "NJ", "UTAH": "UT", "MICHIGAN": "MI", "WEST VIRGINIA": "WV", "WASHINGTON": "WA",
                 "MINNESOTA": "MN", "OREGON": "OR", "VIRGINIA": "VA", "VIRGIN ISLANDS": "VI", "MARSHALL ISLANDS": "MH",
                 "WYOMING": "WY", "OHIO": "OH", "SOUTH CAROLINA": "SC", "INDIANA": "IN", "NEVADA": "NV", "LOUISIANA": "LA",
                 "NORTHERN MARIANA ISLANDS": "MP", "NEBRASKA": "NE", "ARIZONA": "AZ", "WISCONSIN": "WI", "NORTH DAKOTA": "ND",
                 "Armed Forces Europe": "AE", "PENNSYLVANIA": "PA", "OKLAHOMA": "OK", "KENTUCKY": "KY", "RHODE ISLAND": "RI",
                 "DISTRICT OF COLUMBIA": "DC", "ARKANSAS": "AR", "MISSOURI": "MO", "TEXAS": "TX", "MAINE": "ME"}

process.extractOne(query="Minnesotta", choices=state_to_code.keys())  # extract the best match from the list
process.extractOne(query="Alabamazz", choices=state_to_code.keys(), score_cutoff=80)

# create a function that takes each state and returns the abbrev
def abbreviate_state(row):
    state_abbrev = process.extractOne(row["state"], choices=state_to_code.keys(), score_cutoff=80)
    if state_abbrev:
        return(state_to_code[state_abbrev[0]])
    return(np.nan)

# create a column beforehand
df_excel["state_abbrev"] = np.nan
df_excel["state_abbrev"] = df_excel.apply(abbreviate_state, axis=1)

# task 7: complex query in pandas
df1 = pd.DataFrame({'A': [npr.randint(1, 9) for x in range(10)],
                   'B': [npr.randint(1, 9)*10 for x in range(10)],
                   'C': [npr.randint(1, 9)*100 for x in range(10)]})

df1.loc[(df1["B"] > 50) & (df1["C"] != 900), "A"]
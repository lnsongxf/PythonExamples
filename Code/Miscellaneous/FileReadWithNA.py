__author__ = 'tirthankar'

import pandas as pd
import xlrd as xl
import numpy as np

# straight read
pdata = pd.read_csv(
    "Code/Miscellaneous/Data/pwt71_11302012version/pwt71_wo_country_names_wo_g_vars.csv")

# passing a string
pdata2 = pd.read_csv("Code/Miscellaneous/Data/pwt71_11302012version/pwt71_wo_country_names_wo_g_vars.csv",
                     na_values = "AFG")
pdata2["isocode"]

# passing a list
pdata3 = pd.read_csv("Code/Miscellaneous/Data/pwt71_11302012version/pwt71_wo_country_names_wo_g_vars.csv",
                     na_values = ["AFG"])
pdata3["isocode"]

# read the file directly from Excel using xlrd
file_location = "Code/Miscellaneous/Data/pwt71_11302012version/pwt71_vars_forWeb.xls"
xlPWT = xl.open_workbook(file_location)
xlPWT1 = xlPWT.sheet_by_index(0)
xlPWT1.cell_value(3, 1)
xlPWT1.nrows
xlPWT1.ncols

# read file directly using pd.read_excel
pmetadata = pd.read_excel("Code/Miscellaneous/Data/pwt71_11302012version/pwt71_vars_forWeb.xls")














pd.read_csv("Code/Miscellaneous/Data/pwt.csv", na_values = ["na"])






textPWT = """
country         ccode   year     Pop            XRAT    currency ppp    t1
Afghanistan     AFG     1950    8150.368        na      na      na      na
Afghanistan     AFG     1951    8284.473        na      na      na      na
Afghanistan     AFG     1952    8425.333        na      na      na      na
Afghanistan     AFG     1953    8573.217        na      na      na      na
"""

liPWT = textPWT.split("\n")
liPWT = [x.split() for x in liPWT][1:6]
npPWT = np.array(liPWT)

pdPWT = pd.DataFrame(npPWT[1:, :], columns=npPWT[0, :])
pdPWT = pdPWT.replace('na', np.nan, regex=True)
pdPWT = pdPWT.convert_objects(convert_numeric=True)



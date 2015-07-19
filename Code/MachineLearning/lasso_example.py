#==============================================================================
# purpose: example of fitting a LASSO example; based on the DataRobot example here:
#   http://www.datarobot.com/blog/r-getting-started-with-data-science/
# author: tirthankar chakravarty
# created: 5/7/15
# revised: 
# comments:
# 1. The requests library does not support the FTP protocol, need to use a specialised
#   adapter from the ftp libraries.
# 2. /GES/GES12/GES12_Flatfile.zip
#==============================================================================

import requests
from zipfile import ZipFile
import ftplib


ftp_nhtsa = ftplib.FTP(host="ftp.nhtsa.dot.gov")
ftp_nhtsa.cwd("/GES/GES12/")

ftp_nhtsa.retrbinary("RETR %s" % "GES12_Flatfile.zip",
                     open("Data/MachineLearning/somefile", "wb").write)


req_nhtsa = requests.get(url="ftp://ftp.nhtsa.dot.gov/GES/GES12/GES12_Flatfile.zip")
if req_nhtsa.ok:
    z_nhtsa = ZipFile(BytesIO(req_nhtsa.content))
    z_nhtsa.extractall(path="Data/MachineLearning/")


import urllib
urllib.urlretrieve("ftp://ftp.nhtsa.dot.gov/GES/GES12/GES12_Flatfile.zip", "GES12_Flatfile.zip")
__author__ = 'tirthankar'
import zipfile

# list the files within the zip folder
zip_rc2013 = zipfile.ZipFile('Archive/richert_coelho2013.zip')
names_rc2013 = zip_rc2013.namelist()

# extrtact the chapter 3 codes
path_rc2013_3 = zip_rc2013.extract(member=names_rc2013[3], path='Archive/')
zip_rc2013_3 = zipfile.ZipFile(path_rc2013_3)
# zip_rc2013_3.namelist()
zip_rc2013_3.extractall(path='Archive/')


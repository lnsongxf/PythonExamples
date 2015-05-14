# ==============================================================================
# purpose: create a counter over a list
# author: tirthankar chakravarty
# created: 13/5/15
# revised: 
# comments:
#==============================================================================

some_list = ['a', 'b', 'c', 'd', 'e']

for counter, item in enumerate(some_list):
    print("This is the item %s" % item)
    with open("./Code/Miscellaneous/Data/file%s.txt" % counter, 'wt') as file_handle:
        file_handle.write("This is some text")
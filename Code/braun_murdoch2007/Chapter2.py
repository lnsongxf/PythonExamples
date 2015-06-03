#====================================================================
# Purpose: Examples and exercises in Chapter 2 of 'A First Course in Statistical
#   Programming with R', Braun & Murdoch (2007)
# Author: Tirthankar Chakravarty
# Created: 23rd May 2015
# Revised:
# Comments:
#====================================================================

# Example 2.1
def calculate_emi(principal, interest_rate, num_months):
    emi = principal*interest_rate*(1/(1-(1 + interest_rate)**-num_months))
    return(emi)

# test the function
num_months = 10
principal = 1500
interest_rate = 0.01
print(calculate_emi(principal, interest_rate, num_months))

# Example
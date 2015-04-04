#====================================================================
# purpose: Python exercises:
# author: tirthankar chakravarty
# created: 27th march 2015
# revised:
# comments: http://www.ling.gu.se/~lager/python_exercises.html
#====================================================================
#! bin/python3
import itertools as it

def max(num1, num2):
    if num1 > num2:
        return(num1)
    elif num1 == num2:
        print("The two numbers are equal.")
        return(num1)  # tie broken arbitrarily
    else:
        return(num2)

def max_of_any(*args):
    a, b = it.tee(*args)
    next(b, None)
    pairs = izip(a, b)



if __name__ == "__main__":
    # test max()
    print(max(3, 4))
    print(max(3, 3))
    print(max(4, 3))
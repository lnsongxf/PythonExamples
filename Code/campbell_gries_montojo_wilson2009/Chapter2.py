#! /bin/python2.7
#====================================================================
# purpose: script containing solutions to the exercises in chapter 2 of
#   the book
# author: tirthankar chakravarty
# created: 3rd april 2015
# revised:
# comments:
#====================================================================

if __name__ == "__main__":
    # exercise 1
    assert isinstance(9 - 3, int)
    assert isinstance(8*2.5, float)
    assert isinstance(9/2, int)
    assert isinstance(9/-2, int)
    assert isinstance(9 % 2, int)
    assert isinstance(9 % -2, int)
    assert isinstance(-9 % 2, int)
    assert isinstance(9/-2.0, float)
    assert isinstance(4 + 3*5, int)
    assert isinstance((4+3)*5, int)
    
    assert (9 - 3 == 6)
    assert (8*2.5 == 20)
    assert (9/2 == 4)
    assert (9/-2 == -5)
    assert (9 % 2 == 1)
    assert (9 % -2 == -1)
    assert (-9 % 2 == 1)
    assert (9/-2.0 == -4.5)
    assert (4 + 3*5 == 19)
    assert ((4+3)*5 == 35)

    print "End of exercise 1."

    # exercise 2
    x = -17
    print "The unary '+' operator multiplies a variable by +1. It changes x = %i to +x = %i." % (x, +x)

    # exercise 3
    temp = 24.0
    print "Temperature in Celsius: %d; temperature in Fahrenheit: %d." % (temp, 32 + 1.8 * temp)

    #



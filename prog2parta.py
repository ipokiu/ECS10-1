## prog2parta.py
## Andrea Hsieh
## April 11th 2016
##
## Homework assignment 2 part a


## Problem 1

def PQ(i, s, c, pn, pa, d, n):
    """function preparedness computes your preparedness quotient
       if return result is bigger than 1, then you are ok
       i = importance of event from 1 to 10 with 10 being the most important
       s = number of hours of sleep you had last night
       c = number of shots of stimulant consumed
       pn = hours of preparing needed to excel
       pa = hours you actually spent preparing
       d = difficuty of subject matter from 1 to 10 with 10 being the hardest
       n = level of nervousness from 1 to 10 with 10 being the most nervous"""
    return numerator(pa, s, c) / denominator(pn, d, n, i)

def numerator(pa, s, c):
    return 8 * pa * numeratorParenthesis(s, c)

def numeratorParenthesis(s, c):
    return (s + c)

def denominator(pn, d, n, i):
    return 3 * pn * denominatorParenthesis(d, n, i)

def denominatorParenthesis(d, n, i):
    return (d + n + i)


## Problem 2

def min3(a,b,c):
    """function min3 returns the smallest of the three values
       parameter a,b,c are numbers"""
    if a <= b and a <= c:
        return a
    elif b <= c and b <= a:
        return b
    else:
        return c


    

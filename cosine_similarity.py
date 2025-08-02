import math
import csv

def inner_product(x,y):

    sum = 0

    for index in range(len(x)):
        sum += x[index]*y[index]
    
    return sum


def magnitude(num):

    squares_sum = 0

    for i in num:
        squares_sum += i**2
        
    return round(math.sqrt(squares_sum),2)

def cosine_similarity(x,y):

    return round(inner_product(x,y)/(magnitude(x)*magnitude(y)),2)




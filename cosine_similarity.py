import math

def inner_product(x,y):

    sum = 0

    for index in range(len(x)):
        sum += x[index]*y[index]
    
    return sum

x = [1,2,3,4]

y = [4,2,0,0]
print(inner_product(x,y))

def magnitude(num):
    squares_sum = 0

    for i in num:
        squares_sum += i**2
    return round(math.sqrt(squares_sum),2)

print(magnitude(y))

def cosine_similarity(x,y):
    return inner_product(x,y)/ (magnitude(x)*magnitude(y))

print(cosine_similarity(x,y))
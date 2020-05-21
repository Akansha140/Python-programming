#1. Write a for loop to compute the sum of square of x from 0 to 8. What is the value of this sum?

Sum = 0
for x in range(9):
    square = x*x
    Sum = Sum + square
print(Sum)

#Ans: 204

#2. Define a function (addition) that returns the sum of two numbers x and y. Use the function to calculate 2.09 + 8.73

def addition(x,y):
    sum = x + y
    print(sum)
    return sum

addition(2.09, 8.73)

#Ans: 10.82

#3.  Find the 3 errors in the code below. The function sin estimate should calculate an estimate
#    of the sine function at the value x, with an error tolerance of tol. After finding the 3 errors
#    and fixing the code, the variable y should equal 0.09983341666666667

#Corrected Code

import math
def sin_estimate(x,tol=10**-10):
    sin_est = 0
    i = 0
    error = abs(sin_est - math.sin(x))
    while error>tol and i<50:
        sin_est += ((-1)**i)*(x**(2*i+1))/math.factorial(2*i+1)
        error = abs(sin_est - math.sin(x))
        i += 3
    return (sin_est-error)
y = sin_estimate(0.1)
print(y)

#Ans: Error 1 = Missing colon “:” after defining function.
#     Error 2 = Missing import math
#     Error 3 = Missing return(sin_est-error)

# Q4 A bakery sells cupcakes, cookies and pastries. A cupcake costs ', a
# cookie costs €1.00 and a pastry costs €0.80. However, the bakery offers
# discounts if you buy multiple items. If you buy 4-8 cupcakes they cost €1.20
# each, and if you buy more then 8 they are €1.00 each. If you buy 5 or more
# cookies they are €0.80. If you buy more than 3 pastries they are reduced to
# €0.65 each, and reduced further to €0.50 if you buy 10 or more.
# Create a set of nested if/elif/else statements to determine the price of each
# item based on the amount the customer requests and then computes the total # cost of the order.
# Pay attention to the phrasing "more than n", "n or more" one includes the
# value 'n' and the other does not.
# Use your code to determine the total cost of 8 cupcakes, 4 cookies and 12
# pastries.

def bakery(cupcake,cookie,pastry):
    if cupcake >= 4:
        cost_cupcake = cupcake*1.20
    elif cupcake > 8:
        cost_cupcake = cupcake*1
    else:
        cost_cupcake = cupcake*1.50

    if cookie >= 5:
        cost_cookie = cookie*0.80
    else:
        cost_cookie = cookie*1.00

    if pastry >=10:
        cost_pastries = pastry * 0.50
    elif pastry > range(3,10):
        cost_pastries = pastry*0.65
    else:
        cost_pastries = pastry*0.80

    sum = cost_cupcake+cost_cookie+cost_pastries
    return sum


Tot_cost = bakery(8,4,12)
print("total cost of 8 cupcakes, 4 cookies and 12 pastries is",Tot_cost)

#Ans: 19.6
































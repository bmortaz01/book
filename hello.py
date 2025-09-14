# hello.py
#   A program to say 'Hello World' and 
#   convert celcius temperature to fahrenhiet and
#   take average of two numbers and
#   calculate future value of an investment and
#   find quadratic roots.
# by: Behzad Mortazavi

import math

def sayHello():
    print('Hello World again!')

def convertTemp(toFahrenheit=True):
    if toFahrenheit:
        celcius = eval(input('What is the Celcius Temperature? '))
        fahrenhiet = (9/5) * celcius + 32
        print(f'The temperature {celcius:>9.2f}\u00B0C == {fahrenhiet:>.2f}\u00B0F degrees in Fahrenheit.')
    else:
        fahrenhiet = eval(input('What is the Fahrenheit Temperature? '))
        celcius = (fahrenhiet - 32) * (5/9)
        print(f'The temperature {fahrenhiet:>9.2f}\u00B0F == {celcius:>.2f}\u00B0C degrees in Celcius.')
    
def takeAvg():
    print('This program computes the average of two exam scores.')
    score1, score2 = eval(input('Enter two scores separated by comma: '))
    average = float(score1 + score2) / 2.0
    print(f'The average of scores [{score1:.2f}, {score2:.2f}] = {average:.2f}')

def futureVal():
    print('This program calculates future value ')
    print('of an investment after n years.')
    
    principal = eval(input('Enter the initial principal: ') )
    apr = eval(input('Enter the annual interest rate %: ') ) / 100.0
    yrs = eval(input('Enter the number of years: ') )
    future = float(principal * ((1 + apr) ** yrs))
    
    print(f"\nWith principal = {principal:.2f} ")
    print(f"interest rate = {apr * 100:.2f}% ") 
    print(f"after {yrs:.2f} years of investment, ")
    print(f"the future value is: {future:.2f}")

def quadRoot():
    print("This program finds the real and imaginary solutions to a quadratic equation.", end="\n\n")
    
    a, b, c = eval(input("Enter coefficient a, b, c (separated by comma): ")) 
    a = float(a)
    b = float(b)
    c = float(c)
    
    rootOf = b * b - 4 * a * c
    if rootOf > 0:
        discRoot = math.sqrt(rootOf) 
        root1 = (-b + discRoot) / (2 * a) 
        root2 = (-b - discRoot) / (2 * a) 
        
        print("\nReal roots are:")
        print(f"root 1: {root1:.9f}")
        print(f"root 2: {root2:.9f}")
    elif rootOf < 0:
        rootOf = -1 * rootOf
        discRoot = math.sqrt(rootOf) / (2 * a)
        root1 = -b  / (2 * a) 
        
        print("\nImaginary roots are:")
        print(f"root 1: {root1:.9f} + {discRoot:.9f} i")
        print(f"root 2: {root1:.9f} - {discRoot:.9f} i")
    else:
        root1 = -b  / (2 * a) 
        print("\nOnly one Real root:")
        print(f"root 1: {root1:.9f}")

def cast_number(strNumber):
    try:
        casted_number = float(strNumber)
    except ValueError:
        print(f"Couldn't cast {repr(strNumber)} to a number.")
        return ''
    else:
        print(f"Casting {repr(strNumber)} to {casted_number}")
        return casted_number
    
def todaysTemp():
    try:
        x = eval(input('Enter today’s temperature in Celsius degrees? '))
    except Exception:
        print("Please enter a numeric value!")
    else:
        if isinstance(x, int) or isinstance(x, float):
            if x < 10:
                print(f"You entered {x:.1f} degrees. It's cold!")
            elif x <= 25:
                print(f"You entered {x:.1f} degrees. It's cool!")
            elif x > 25:
                print(f"You entered {x:.1f} degrees. It's hot!")
        else:
            print("Please enter a numeric value!")

if __name__ == '__main__':
    sayHello()

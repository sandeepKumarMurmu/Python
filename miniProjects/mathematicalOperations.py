import math

# radius = float(input(f'Enter the radius of the circle : '));

# print(f'Area of circle if {2*math.pi*(radius**2)}')

operator = input('Please select operator (+, -, *, /) :');
n1 = float(input("Please enter first number : "))
n2 = float(input("Please enter second number : "))

if(operator == '+'):
        print(f"sum of two number is {n1+n2}")
elif(operator == "*"):
        print(f"multiplication of two number is {n1*n2}")
elif(operator == "-"):
        print(f"Substraction of two number is {n1-n2}")
elif(operator == "/"):
        print(f"Division of two number is {n1/n2}")
else:
        print("Invalid operator selected.")
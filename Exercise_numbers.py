print("This program will calculate the area and cicumference of a circle")

import math

radius = float(input("The radiuus of the circle:"))
area = math.pi * (radius**2)
circumference = 2 * math.pi * radius

print("The area of the circle is:",round(area,2))
print("The circumference of the circle is",round(circumference,2))

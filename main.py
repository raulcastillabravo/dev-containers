import math
import pandas as pd

print('Hello from Dev Container')

def calculate_circle_area(radius):
    return math.pi * radius**2

radius = 5.0

area = calculate_circle_area(radius)

print(f"The area of the circle with radius {radius} is: {area:.2f}")

df = pd.DataFrame({
    'A': [1,2,3],
    'B': [4,5,6]
})

print(df)
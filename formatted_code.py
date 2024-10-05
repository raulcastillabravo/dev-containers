import json
import math
import os
import random
import re
import sys
import time

import numpy as np
import pandas as pd


def calculate_circle_area(radius):
    return math.pi * radius**2


def generate_random_radius(min_radius, max_radius):
    return random.uniform(min_radius, max_radius)


radii = [generate_random_radius(1, 10) for _ in range(10)]
areas = [calculate_circle_area(radius) for radius in radii]
for i in range(len(radii)):
    print(f"Circle {i+1}: radius={radii[i]:.2f}, area={areas[i]:.5f}")


def print_summary(radii, areas):
    total_area = sum(areas)
    avg_radius = sum(radii) / len(radii)
    print(f"Total area is {total_area:.5f}. Average radius is {avg_radius:.3f}")


random_radius = generate_random_radius(5, 15)
new_area = calculate_circle_area(random_radius)
print(f"A new random circle with radius={random_radius:.3f} has area={new_area:.5f}")
print_summary(radii, areas)

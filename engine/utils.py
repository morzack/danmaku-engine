import math

def clamp(x, min_num, max_num):
    return max(min_num, min(max_num, x))

def check_bounds(x, min_x, max_x):
    return min_x < x < max_x

def calculate_angle(point_a, point_b):
    return math.atan2(point_b[1]-point_a[1], point_b[0]-point_a[0])

def raduis_collision(position_a, radius_a, position_b, radius_b):
    d = math.sqrt((position_a[0]-position_b[0])**2+(position_a[1]-position_b[1])**2)
    x = abs(position_a[0] - position_b[0])
    y = abs(position_a[1] - position_b[1])
    r = (radius_a+radius_b)
    a = d < r
    return a
def calculate_distance(x1, y1, x2, y2):

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

# Example usage:
x1, y1 = float(input("Enter x coordinate of point 1: ")), float(input("Enter y coordinate of point 1: "))
x2, y2 = float(input("Enter x coordinate of point 2: ")), float(input("Enter y coordinate of point 2: "))

distance = calculate_distance(x1, y1, x2, y2)

print("The distance between the two points is:", distance)

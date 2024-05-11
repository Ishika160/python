a = float(input("Enter the length of side 1: "))
b = float(input("Enter the length of side 2: "))
c = float(input("Enter the length of side 3: "))

# Semi-perimeter of the triangle
    s = (a + b + c) / 2
    
    # Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
    print(area)

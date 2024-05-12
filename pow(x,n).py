class PowerCalculator:
    def __init__(self, base):
        self.base = base

    def pow(self, exponent):
        result = 1
        for _ in range(exponent):
            result *= self.base
        return result

# Example usage:
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

power_calculator = PowerCalculator(base)
result = power_calculator.pow(exponent)
print("Result:", result)

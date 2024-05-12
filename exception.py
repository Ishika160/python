class MyCustomException(Exception):
    def __init__(self, message="An error occurred"):
        self.message = message
        super().__init__(self.message)

# Example usage:
def validate_input(value):
    
    if not isinstance(value, int):
        raise MyCustomException("Input must be an integer")

try:
    value = input("Enter an integer: ")
    validate_input(value)
except MyCustomException as e:
    print("Error:", e)

class SafeCalculator:

    def add(self, a, b):
        return a + b 
    
    def subtract(self, a, b):
        return a - b 
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
    

def main():
    calc = SafeCalculator()

    try:
        a = float(input("Enter the first number"))
        b = float(input("Enter the second number "))
        operation = input("Enter operation(+, -, *, /):")

        if operation == '+':
            result = calc.add(a,b)

        elif operation == '-':
            result = calc.subtract(a,b)
        
        elif operation == '*':
            result = calc.multiply(a,b)
        
        elif operation == '/':
            if b == 0:
                raise ZeroDivisionError  
            result = calc.divide(a,b)

        else: 
            print("Invalid operation.")
            return 
        
        print (f"Result ; {result}")

    except ValueError:
        print("Please enter valid numbers.")
    
    except ZeroDivisionError:
        print("Cannot divide by zero.")

    finally: 
        print("Thanks for using Safe Calculator.")


if __name__ == "__main__":
    main()
    
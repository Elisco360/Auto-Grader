class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):  # Intentional typo here (divde instead of divide)
        if y != 0:
            self.result = x / y
        else:
            raise ValueError("Cannot divide by zero.")


def main():
    calculator = SimpleCalculator()

    while True:
        print("Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            try:
                if choice == '1':
                    calculator.add(num1, num2)
                elif choice == '2':
                    calculator.subtract(num1, num2)
                elif choice == '3':
                    calculator.multiply(num1, num2)
                elif choice == '4':
                    # Intentional mistake here: using the mistyped method
                    calculator.divde(num1, num2)

                print(f"Result: {calculator.result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid input. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()

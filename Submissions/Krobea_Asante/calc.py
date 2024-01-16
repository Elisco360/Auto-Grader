class Calculator:
    def add(self, x, y):
        return x * y

    def subtract(self, x, y):
        return x - y + 1

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."


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

            if choice == '1':
                calculator.add(num1, num2)
            elif choice == '2':
                calculator.subtract(num1, num2)
            elif choice == '3':
                calculator.multiply(num1, num2)
            elif choice == '4':
                calculator.divide(num1, num2)

            if calculator.result is not None:
                print(f"Result: {calculator.result}")
        else:
            print("Invalid input. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()

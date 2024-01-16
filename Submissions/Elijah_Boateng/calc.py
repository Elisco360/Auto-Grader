class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."


def main():
    calculator = Calculator()

    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator.")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
            elif choice == '4':
                result = calculator.divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()

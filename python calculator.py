import random

def calculator():
    print("🎉 Welcome to the Fun Calculator! 🎉")
    print("-----------------------------------")

    while True:
        # Get input from the user
        try:
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numeric values.")
            continue

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Surprise Me! 🎲")

        operation = input("Enter the number corresponding to the operation (1/2/3/4/5): ")

        # Perform the chosen operation
        if operation == '1':
            result = num1 + num2
            op = '+'
        elif operation == '2':
            result = num1 - num2
            op = '-'
        elif operation == '3':
            result = num1 * num2
            op = '*'
        elif operation == '4':
            if num2 == 0:
                print("❌ Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
            op = '/'
        elif operation == '5':
            surprise_options = [
                ("square of first number", num1 ** 2),
                ("square of second number", num2 ** 2),
                ("average", (num1 + num2) / 2),
                ("percentage (num1% of num2)", (num1 / 100) * num2),
                ("random choice between num1 and num2", random.choice([num1, num2]))
            ]
            surprise = random.choice(surprise_options)
            print(f"\n🎁 Surprise Operation: {surprise[0]}")
            print(f"Result: {surprise[1]}")
        else:
            print("❌ Invalid operation choice.")
            continue

        # Only show normal operation result if not surprise
        if operation in ['1', '2', '3', '4']:
            print(f"\n✅ Result: {num1} {op} {num2} = {result}")

        # Ask to continue
        cont = input("\n🔁 Do you want to perform another calculation? (y/n): ").lower()
        if cont != 'y':
            print("👋 Thanks for using the Fun Calculator. Goodbye!")
            break

# Run the calculator
calculator()

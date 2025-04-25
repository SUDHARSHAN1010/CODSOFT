import random
import string

def generate_password():
    print("🔐 Welcome to the Password Generator!")
    print("-------------------------------------")

    while True:
        # Get desired length from user
        try:
            length = int(input("\nEnter the desired password length: "))
            if length < 4:
                print("❌ Password length should be at least 4 for strong security.")
                continue
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        # Define possible characters
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display result
        print(f"\n✅ Your secure password is: {password}")

        # Ask if the user wants another one
        again = input("\n🔁 Generate another password? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for using the Password Generator. Stay secure!")
            break

# Run the password generator
generate_password()

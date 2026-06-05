import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation

def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length < 8:
        return "Weak ❌"
    elif length >= 12 and score == 4:
        return "Strong ✓"
    else:
        return "Medium ⚠️"

print("--- Password Manager ---")

while True:
    print("\n1. Generate a random password")
    print("2. Create my own password")
    print("3. Check password strength")
    print("4. Quit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        try:
            length = int(input("Enter password length: "))
            if length < 8:
                print("Password length should be at least 8!")
            else:
                password = ''.join(secrets.choice(characters) for i in range(length))
                print(f"\nYour generated password: {password}")
                print(f"Password length: {length} characters")
                print(f"Password strength: {check_strength(password)}")
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "2":
        password = input("Enter your own password: ")
        strength = check_strength(password)
        if strength == "Weak ❌":
            print("Weak password! Should be at least 8 characters.")
        else:
            print(f"Password saved: {password}")
            print(f"Password strength: {strength}")

    elif choice == "3":
        password = input("Enter password to check: ")
        length = len(password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in string.punctuation for c in password)

        print(f"\n--- Password Analysis ---")
        print(f"Length: {length} characters")
        print(f"Uppercase letters: {'✓' if has_upper else '✗'}")
        print(f"Lowercase letters: {'✓' if has_lower else '✗'}")
        print(f"Numbers: {'✓' if has_digit else '✗'}")
        print(f"Symbols: {'✓' if has_symbol else '✗'}")
        print(f"Strength: {check_strength(password)}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
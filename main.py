import random
import string
import secrets
from pyperclip import copy

def generate_password(length=12):
    if length < 8:
        print("Warning: Short passwords are not secure. Using minimum length of 8.")
        length = 8

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special_chars)
    ]

    all_chars = lowercase + uppercase + digits + special_chars
    password.extend(secrets.choice(all_chars) for _ in range(length - 4))

    random.shuffle(password)

    return ''.join(password)

def main():
    while True:
        try:
            user_input = input("Enter desired password length (or 'q' to quit): ")

            if user_input.lower() == 'q':
                print("Goodbye!")
                break

            length = int(user_input)
            password = generate_password(length)
            copy(password)
            print(f"Your password is copied to clipboard: {password}")

        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break

if __name__ == "__main__":
    main()

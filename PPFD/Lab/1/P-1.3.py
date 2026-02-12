import secrets
import string
import random

def generate_strong_password(length):
    if length < 4:
        print("Warning: Password length is too short for a strong password. Minimum recommended is 4.")
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    all_chars = lower + upper + digits + punctuation
    password = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(punctuation)
    ]

    remaining_length = length - 4
    if remaining_length > 0:
        for _ in range(remaining_length):
            password.append(secrets.choice(all_chars))
    if length < 4:
        password = password[:length]
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        user_input = input("Enter the number for generating a randomized password: ")
        length = int(user_input)
        
        if length <= 0:
            print("Please enter a positive integer.")
            return

        pwd = generate_strong_password(length)
        print(f"Generated Password: {pwd}")
        
    except ValueError:
        print("Invalid input! Please enter a valid integer number.")

if __name__ == "__main__":
    main()
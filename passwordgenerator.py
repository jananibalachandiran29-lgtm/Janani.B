import secrets
import string
import math

last_password = None

CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def theme():
    print(CYAN + """
╔══════════════════════════════════════════════╗
║        🔐  PASSWORD GENERATOR PRO  🔐        ║
║               by Janani ✨                   ║
╚══════════════════════════════════════════════╝
""" + RESET)

def calculate_entropy(length, charset_size):
    if charset_size == 0:
        return 0
    return length * math.log2(charset_size)


def entropy_to_strength(entropy):
    if entropy < 40:
        return "WEAK"
    elif entropy < 60:
        return "MEDIUM"
    elif entropy < 80:
        return "STRONG"
    else:
        return "VERY STRONG"


def generate_password():
    global last_password
    theme()
    print("--- Generate Password ---\n")

    try:
        length = int(input("Enter password length (8–128): "))
    except ValueError:
        print("Error: Please enter a valid number!")
        return

    if not (8 <= length <= 128):
        print("Error: Length must be between 8 and 128.")
        return

    use_lower = input("Include lowercase? (y/n): ").lower() == "y"
    use_upper = input("Include uppercase? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    if not (use_lower or use_upper or use_digits or use_symbols):
        print("Error: At least one character type must be selected!")
        return

    pool = ""
    if use_lower:
        pool += string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += "!@#$%^&*_-+=?"

    password = "".join(secrets.choice(pool) for _ in range(length))

    entropy = calculate_entropy(length, len(pool))
    strength = entropy_to_strength(entropy)

    print("\n✔ Password Generated:")
    print(password)
    print(f"🔒 Strength: {strength}")

    last_password = password


def view_last_password():
    theme()
    print("--- Last Generated Password ---\n")

    if last_password is None:
        print("No password generated yet.")
    else:
        print("Last Password:", last_password)


def save_to_file():
    theme()
    print("--- Save Password to File ---\n")

    if last_password is None:
        print("No password to save! Generate one first.")
        return

    with open("password.txt", "w") as f:
        f.write("Password Generator Pro by Janani\n")
        f.write("===============================\n\n")
        f.write("Last Generated Password:\n")
        f.write(last_password)

    print("✔ Password saved to password.txt")


def menu():
    while True:
        theme()
        print("1. Generate Password")
        print("2. View Last Generated Password")
        print("3. Save to File")
        print("4. Exit")

        choice = input("\nEnter your choice (1–4): ")

        if choice == "1":
            generate_password()
        elif choice == "2":
            view_last_password()
        elif choice == "3":
            save_to_file()
        elif choice == "4":
            print("\nThank you for using Password Generator Pro !")
            break
        else:
            print("Invalid choice! Please enter 1–4.")


if __name__ == "__main__":
    menu()

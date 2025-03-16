import string

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():  # Process only letters
            shift_amount = shift if mode == "encrypt" else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

def main():
    print("""
    ========================================
    |  |   |   CAESAR CIPHER TOOL   |   |   |
    ========================================
    Encrypt and Decrypt messages securely
    """)
    
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ").strip()
        
        if choice == "3":
            print("Exiting program. Goodbye!")
            break
        elif choice not in ["1", "2"]:
            print("Invalid choice! Please select a valid option.")
            continue
        
        mode = "encrypt" if choice == "1" else "decrypt"
        text = input("Enter your message: ")
        
        while True:
            try:
                shift = int(input("Enter shift value (1-25): "))
                if 1 <= shift <= 25:
                    break
                else:
                    print("Shift value must be between 1 and 25.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        output = caesar_cipher(text, shift, mode)
        print(f"\n{mode.capitalize()}ed message: {output}\n")
        
        again = input("Do you want to run again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the Caesar Cipher Tool!")
            break

if __name__ == "__main__":
    main()

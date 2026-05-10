import string
 
def encrypt(message, shift):
    encrypted_text = ""
    for character in message:
        if character.isupper():
            encrypted_text += chr((ord(character) - ord('A') + shift) % 26 + ord('A'))
        elif character.islower():
            encrypted_text += chr((ord(character) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += character
    return encrypted_text
 
def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)
 
def display_alphabet_shift(shift):
    alphabet = string.ascii_uppercase
    shifted = alphabet[shift % 26:] + alphabet[:shift % 26]
    print("\n  Alphabet shift chart (uppercase):")
    print("  Original :", " ".join(alphabet))
    print("  Shifted  :", " ".join(shifted))
 
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Please enter a whole number (e.g. 3, 13, 25).")
 
def main():
    print("=" * 55)
    print("         CAESAR CIPHER ENCRYPTOR / DECRYPTOR")
    print("=" * 55)
 
    message = input("\n  Enter your message: ")
    shift = get_integer_input("  Enter shift value  (e.g. 3): ") % 26
 
    display_alphabet_shift(shift)
 
    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)
 
    print()
    print("=" * 55)
    print(f"  Original message  : {message}")
    print(f"  Shift value       : {shift}")
    print(f"  Encrypted message : {encrypted}")
    print(f"  Decrypted message : {decrypted}")
    print("=" * 55)
 
    if decrypted == message:
        print("\n  Success! Decryption matches the original message.\n")
    else:
        print("\n  Something went wrong — messages don't match.\n")
 
if __name__ == "__main__":
    main()
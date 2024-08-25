# Encryption and Decryption Using Ceaser Cipher
def ceaser_cipher(text, shift, encrypt = True):
    shift = shift if encrypt else -shift
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) %26 + start)
        else:
            result += char
    return result

# Encryption and Decryption Using Vigenere Cipher
def vigenere_cipher(text, key, encrypt = True):
    key = key.lower()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            shift = shift if encrypt else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
            key_index += 1
        else:
            result += char
    return result

# Encryption and Decryption Using Atbash Cipher
def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(ord('Z')- (ord(char)-ord('A')))
            else:
                result += chr(ord('z')- (ord(char)-ord('a')))
        else:
            result += char
    return result


# User input to choose which cipher is to be used for encryption/decryption of text
choice = input("Choose a cipher(Ceaser or Vigenere or Atbash): ").strip().lower()

# User input for the text
text = input("Enter text: ")

if choice == "ceaser":
    shift = int(input("Enter Shift(e.g. 3): "))
    action = input("Encrypt or Decrypt? (E/D): ").strip().upper()
    encrypt = True if action == 'E' else False
    result = ceaser_cipher(text, shift, encrypt)
elif choice == "vigenere":
    key = input("Enter a Key(e.g. Help): ")
    action = input("Encrypt or Decrypt? (E/D): ").strip().upper()
    encrypt = True if action == "E" else False
    result = vigenere_cipher(text, key, encrypt)
elif choice == "atbash":
    result = atbash_cipher(text)
else:
    result = "Invalid Cipher Choice."

print(f"Result: {result}")
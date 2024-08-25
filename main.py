# Encryption and Decryption Using caesar Cipher
def caesar_cipher(text, shift, encrypt = True):
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

# Encryption and Decryption using XOR Cipher
def xor_cipher(text, key):
    result = ""
    for i in range(len(text)):
        result += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return result

# Encryption and Decryption Using Rail-Fence Cipher
def rail_fence_cipher(text, key, encrypt = True):
    if encrypt:
        rail =[''] * key
        row = 0
        direction = 1
        for char in text:
            rail[row] += char
            if row == 0:
                direction = 1
            elif row == key - 1:
                direction = -1
            row += direction
        return ''.join(rail)
    else:
        rail = [''] * key
        idx = 0
        direction = 1
        length = [0] * key
        row = 0
        for char in text:
            length[row] += 1
            if row == 0:
                direction = 1
            elif row == key - 1:
                direction = -1
            row += direction
        for r in range(key):
            rail[r] = text[idx:idx + length[r]]
            idx += length(r)
        result = ""
        row = 0
        direction = 1
        for i in range(len(text)):
            result += rail[row][0]
            rail[row] = rail[row][1:]
            if row == 0:
                direction = 1
            elif row == key - 1:
                direction = -1
            row += direction
        return result

# Encryption and Decryption using Playfair Cipher
def playfair_cipher(text, key, encrypt = True):
    def generate_table(key):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        table = []
        used = set()
        for char in key.upper() +alphabet:
            if char not in used and char != 'J':
                table.append(char)
                used.add(char)
        return [table[i:i+5] for i in range(0, 25, 5)]

    def find_position(char, table):
        for i, row in enumerate(table):
            if char in row:
                return  i, row.index(char)
        return None, None

    def prepare_text(text):
        text = text.upper().replace("J", "I")
        prepared = ""
        i = 0
        while i < len(text):
            if i + 1 < len(text) and text[i] == text[i + 1]:
                prepared += text[i] + "X"
                i += 1
            else:
                prepared += text[i:i+2]
                i += 2
        if len(prepared) % 2 != 0:
            prepared += "X"
        return prepared

    table = generate_table(key)
    prepare_text = prepare_text(text)
    result = ""

    for i in range(0, len(prepare_text), 2):
        row1, col1 = find_position(prepare_text[i], table)
        row2, col2 = find_position(prepare_text[i + 1], table)
        if row1 == row2:
            if encrypt:
                result += table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5]
            else:
                result += table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            if encrypt:
                result += table[(row1 + 1) % 5][col1] + table[(row2 + 1) % 5][col2]
            else:
                result += table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]
        else:
            result += table[row1][col1] + table[row2][col2]
    return result

# Encryption and Decryption using Block Cipher
def block_cipher(text, key, encrypt = True):
    # The below program is Highly simplified version of DES, only for Education Purpose
    def permute(bits, permutation):
        return ''.join(bits[i] for i in permutation)

    def f_k(bits, key):
        return ''.join(str((int(b) ^ int(k)) & 1) for b, k in zip(bits, key))

    def des_round(text, key, encrypt = True):
        L, R = text[:4], text[4:]
        if encrypt:
            return R + f_k(L, key)
        else:
            return f_k(R, key) + L

    permutation = [1, 4, 2, 3, 6, 5, 0, 7] #example of Initial Permutation
    permuted_text = permute(text, permutation)
    round_key = key[:4]    #simplistic key scheduling
    if encrypt:
        return des_round(permuted_text, round_key)
    else:
        return des_round(permuted_text, round_key, encrypt=False)

def main():
    print("Multi-Cipher Encryption Tool")
    print("1. Caesar Cipher")
    print("2. Vigenere Cipher")
    print("3. Atbash Cipher")
    print("4. XOR Cipher")
    print("5. Rail Fence Cipher")
    print("6. Playfair Cipher")
    print("7. Block Cipher")

    choice = input("Choose a cipher (1-7): ").strip()

    if choice not in [str(i) for i in range(1,8)]:
        print("Invalid Choice. Please select 1-7")
        return
    text = input("Enter the Text: ")

    if choice == '1':
        shift = int(input("Enter the shift (e.g. 3): "))
        action = input("Encrypt or Decrypt? (E/D): ").strip().upper()
        encrypt = True if action == 'E' else False
        result = caesar_cipher(text, shift, encrypt)
    elif choice == '2':
        key = input("Enter the key (e.g., SECRET): ")
        action = input("Encrypt or Decrypt? (E/D): ").strip().upper()
        encrypt = True if action == 'E' else False
        result = vigenere_cipher(text, key, encrypt)
    elif choice == '3':
        result = atbash_cipher(text)
    elif choice == '4':
        key = input("Enter the key (e.g., XORKEY): ")
        result = xor_cipher(text, key)
    elif choice == '5':
        key = int(input("Enter the key (e.g., 3): "))
        action = input("Encrypt or Decrypt? (E/D): ").strip().upper()
        encrypt = True if action == 'E' else False
        result = rail_fence_cipher(text, key, encrypt)
    elif choice == '6':
        key = input("Enter the key (e.g., PLAYFAIR): ")
        action = input("Encrypt or Decrypt? (E/D): ").strip().upper()
        encrypt = True if action == 'E' else False
        result = playfair_cipher(text, key, encrypt)
    elif choice == '7':
        binary_text = ''.join(format(ord(c), '08b') for c in text)
        binary_key = ''.join(format(ord(c), '08b') for c in input("Enter a 4-bit key (e.g., 1010): "))
        action = input("Encrypt or Decrypt? (E/D): ").strip().upper()
        encrypt = True if action == 'E' else False
        result = block_cipher(binary_text, binary_key, encrypt)
        result = ''.join(chr(int(result[i:i + 8], 2)) for i in range(0, len(result), 8))

    print(f"Result: {result}")

# Deployment of main function 
if __name__ == "__main__":
    main()
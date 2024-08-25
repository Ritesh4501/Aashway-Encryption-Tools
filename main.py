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
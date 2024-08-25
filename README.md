# Multi-Cipher Encryption Tool
Simple Encryption and Decryption tool using Multiple Ciphers 

In this Project, I have implemented Multiple Ciphers for Encryption and Decryption. 
It is a Python-based tool which provides a simple way to encrypt and decrypt messages using various classical and basic cryptographic algorithm.  
This Tools support multiple ciphers, including Ceaser, Vigenere, Atbash, XOR, Rail Fence, Play-Fair, Block Cipher.  
This is the first task of my as a part of Cyber Security Internship at **Aashway**.  
The project challenged me to design a flexible system capable of handling various cipher techniques, each with its unique encryption and decryption processes.
Working on this tool has greatly deepened my understanding of cryptographic principles, algorithm design, and secure communication.  
I’m eager to continue building upon this foundation and explore more advanced cryptography concepts in the future!

## Features
- **Block Cipher (Using Simple DES-Like)**: It is a Simplified version of DES algorithm which is use for educational purposes only.


- **Ceaser Cipher**: It is similar as Substitution Cipher, in which it shifts a letter in the text by a fixed number of positions in the alphabet.


- **Vigenere Cipher**: It uses a keyword to shift letters in the text, providing a poly-alphabetic encryption scheme.


- **Atbash Cipher**: It maps each letter of alphabet to its reverse.


- **XOR Cipher**: It encrypt character in the text by XORing it with the key.


- **Rail Fence Cipher**: It arranges text in zig-zag pattern and read it row by row.


- **Playfair Cipher**: It encrypt pairs of letters by using 5x5 table created from the keyword.

# Getting Started 
## Prerequisites

- **Python 3.x**: Ensure you have installed Python 3.x installed in your system. You can download it from [python.org](https://www.python.org/)

### Installation 

1. **Clone the Repository**:  
    ```bash
   git clone https://github.com/Ritesh4501/Aashway-Encryption-Tools.git
   cd Encryption-Tools
   ```
2. **Run the Script**:
    ```bash
    python3 main.py
   ```
## Usage
1. **Run the tool**:
    - Execute the python script using your terminal or command prompt.
2. **Select a Cipher**:
    - Choose from the list of available ciphers by entering the corresponding number.
3. **Input Your Text**:
    - Enter the text you want to encrypt or decrypt.
4. **Provisional Additional Information**:
    - Depending on the selected cipher, you may need to provide key, shift value, or choose between encryption and decryption.
5. **View the Result**:
    - The tool will display the encrypted or decrypted text based on your inputs.

## Example
**Encrypting with Ceaser Cipher**
1. **Select Cipher**: Choose option `1` for Ceaser Cipher.
2. **Enter Text**: Input `HELLO`.
3. **Enter Shift**: Provide a shift value, such as `3`.
4. **Encrypt**: The tool outputs `KHOOR`

**Encrypting with Vigenere Cipher**
1. **Select Cipher**: Choose option `2` for Vigenere Cipher.
2. **Enter Text**: Input `HELLO`.
3. **Enter Key**: Provide a key word, such as `SECRET`.
4. **Encrypt**: The tool outputs `RIJVS`

# Contributing
Contributions are welcome! If you have suggestions for additional features, improvements, or new ciphers, feel free to submit a pull request.

# License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
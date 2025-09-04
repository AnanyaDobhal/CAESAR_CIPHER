# CAESAR_CIPHER 🔐

This is a simple C++ implementation of the Caesar Cipher, one of the oldest and simplest encryption techniques.

## 📌 Features
Encrypts and decrypts text using Caesar Cipher.
Preserves case (uppercase/lowercase).

Ignores non-alphabetic characters (numbers, punctuation remain unchanged).
## 🖥️ Usage
1. Compile the program
g++ caesar_cipher.cpp -o caesar_cipher

2. Run the program
./caesar_cipher

3. Input Format

The program expects three inputs:

Mode → encrypt or decrypt

Text → message to encrypt/decrypt

Shift value → integer shift amount

## 🔹 Example 1: Encryption

Input

encrypt
HELLO WORLD
3


Output

KHOOR ZRUOG

## 🔹 Example 2: Decryption

Input

decrypt
KHOOR ZRUOG
3


Output

HELLO WORLD

# Caesar Cipher
# The Caesar cipher shifts each letter forward in the alphabet by
# the key. The resulting message has all the letters advanced by 'key'
# positions.
# To run the code, execute the main() function.

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    for letter in message:
        if alpha.find(letter) >= 0:  # Check to see if the character is a letter
            spot = (alpha.find(letter) + key) % 26
            secret += alpha[spot]
        else:  # Character must be a number, symbol, or punctuation
            secret += letter

    return secret

def decode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    plaintext = ""

    for letter in message:
        if alpha.find(letter) >= 0:  # Check to see if the character is a letter
            spot = (alpha.find(letter) - key) % 26
            plaintext += alpha[spot]
        else:  # Character must be a number, symbol, or punctuation
            plaintext += letter

    return plaintext

def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))

    secret = encode(message, key)
    print("Encrypted:", secret)
    plaintext = decode(secret, key)
    print("Decrypted:", plaintext)

if __name__ == '__main__':
    main()


def caesar_cipher(text, shift, encode=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    result = []

    for char in text:
        is_uppercase = char.isupper()
        char = char.lower()

        if char in alphabet:
            index = alphabet.index(char)
            if encode:
                new_char = shifted_alphabet[index]
            else:
                new_char = alphabet[shifted_alphabet.index(char)]

            if is_uppercase:
                new_char = new_char.upper()
        else:
            new_char = char

        result.append(new_char)

    return ''.join(result)

# Get user input
user_text = input("Enter the sentence you want: ")
shift = int(input("Enter the shift value: "))

# Get user's choice for encoding or decoding
user_choice = input("Enter 'True' to encode or 'False' to decode: ")
encode = user_choice.strip().lower() == 'true'

# Encrypt or decrypt the user's input based on their choice
processed_text = caesar_cipher(user_text, shift, encode=encode)
if encode:
    print("Encrypted text:", processed_text)
else:
    print("Decrypted text:", processed_text)


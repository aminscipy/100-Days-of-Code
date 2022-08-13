

should_continue = True
while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26


    def encrypt():
        list(text)
        cipher_text = ''
        for letter in text:
            if letter in alphabet:
                letter_index = alphabet.index(letter)
                letter_index += shift
                cipher_text += alphabet[letter_index]
            else:
                cipher_text += letter
        print(cipher_text)


    def decrypt():
        list(text)
        cipher_text = ''
        for letter in text:
            if letter in alphabet:
                letter_index = alphabet.index(letter)
                letter_index -= shift
                cipher_text += alphabet[letter_index]
            else:
                cipher_text += letter
        print(cipher_text)


    if direction == 'encode':
        encrypt()
    elif direction == 'decode':
        decrypt()

    want_to_stop = input(" want to continue? type 'yes' to continue and 'no' to stop\n")
    if want_to_stop == 'no':
        should_continue = False
        print('Goodbye')

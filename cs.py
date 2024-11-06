def caesar_decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

message = "N qtaj uwtlwfrrnsl zxnsl Udymts"
shift_key = 5
decrypted_message = caesar_decrypt(message, shift_key)
print("Decrypted message:", decrypted_message)







def caesar_decrypt(message, shift_key):
    decrypted_message = ''

    for char in message:
        if char.isalpha():

            if char.islower():

                shift = ord('a')

            else:

                shift = ord('A')

            decrypted_char = chr((ord(char) - shift - shift_key) % 26 + shift)

        else:
            
            decrypted_char += char

        
        return decrypted_char
    

message = 'N qtaj uwtlwfrrnsl zxnsl Udymts'

shift_key = 5

print('Decrypted message: ', caesar_decrypt(message, shift_key))
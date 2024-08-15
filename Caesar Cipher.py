def caesar_cipher(text, shift, mode='encrypt'):
    shift = shift if mode == 'encrypt' else -shift
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result
def main():
    while True:
        mode = input("Do you want to Encrypt or Decrypt a message? (E/D): ").upper()
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        result = caesar_cipher(message, shift, 'encrypt' if mode == 'E' else 'decrypt')
        print(f"Result: {result}")
        if input("Process another message? (Y/N): ").upper() == 'N':
            break
if __name__ == "__main__":
    main()
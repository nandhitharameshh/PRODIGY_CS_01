def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char

    return result


def main():
    print("=== Caesar Cipher ===")

    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    choice = input("Choose operation (encrypt/decrypt): ").strip().lower()

    if choice not in ("encrypt", "decrypt"):
        print("Invalid operation.")
        return

    result = caesar_cipher(message, shift, choice)

    print(f"\nResult: {result}")


if __name__ == "__main__":
    main()
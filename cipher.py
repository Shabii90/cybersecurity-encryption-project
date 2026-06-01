def encode_message(message):
    encoded = ""

    for char in message:
        # Check if character is a letter
        if char.isalpha():
            # Handle lowercase letters
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')

            # Convert letter to number, shift by 15, wrap using modulo
            new_char = chr((ord(char) - base + 15) % 26 + base)

            encoded += new_char
        else:
            # Keep spaces and punctuation unchanged
            encoded += char

    return encoded


# Get input from user
message = input("Enter your message:")

# Encode message

result = encode_message(message)

# Print result
print("Encoded message:", result)
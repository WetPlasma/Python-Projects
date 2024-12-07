alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print("""
      _,-._
    .'     `.
   /   O   \
  |    ^    |
  \  `-'  /
   `-----'
     /|\
    / | \
   /  |  \
  /   |   \
 /____|____\
""")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    output = []
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if direction == "encode":
                index += shift % 26
            elif direction == "decode":
                index -= shift % 26
            output.append(alphabet[index])
        else:
            output.append(char)  # Keep non-alphabetic characters as is
    output = ''.join(output)
    if direction == "encode":
        print(f"The encoded text is {output}")
    elif direction == "decode":
        print(f"The decoded text is {output}")

caesar(text, shift, direction)

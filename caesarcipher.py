alphabets_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                   "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                   "y", "z"]
alphabets_upper = [i.upper() for i in alphabets_lower]


def encode():
    result = ""
    encode_text = input("Enter the text that you want to encode: ")  # sahil
    shift = int(input("Enter Shift value: "))
    for i in encode_text:
        if i.islower():
            index = alphabets_lower.index(i)
            index += shift
            result += alphabets_lower[index]
        else:
            index = alphabets_upper.index(i)
            index += shift
            result += alphabets_upper[index]
    print(f"The encoded result is {result}")


def decode():
    result = ""
    decode_text = input("Enter the encoded text that you want to decode: ")
    shift = int(input("Enter Shift value: "))
    for i in decode_text:
        if i.islower():
            index = alphabets_lower.index(i)
            index -= shift
            result += alphabets_lower[index]
        else:
            index = alphabets_upper.index(i)
            index -= shift
            result += alphabets_upper[index]
    print(f"The decoded result for {decode_text} is {result}")


def main():
    while True:
        ch = int(input(""" 
Welcome to Caesar Cipher
1. Encode your message (Type 1)
2. Decode your message (Type 2)
3. Exit (Type 3)
        """))
        if ch == 1:
            encode()
        elif ch == 2:
            decode()
        elif ch == 3:
            break
        else:
            print("Wrong Input!! Try Again!!!")


main()

#Encode/Decode program

#Encoder, receives str of numbers of any length, returns int where each digit has been increased by three.
def encode(input_num):
    encoded_num = ''
    for digit in str(input_num):
        encoded_digit = int(digit) + 3
        encoded_num += str(encoded_digit)[-1]
    return int(encoded_num)

def decode(encoded_num):
    pass

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        try:
            menu_option = int(input("Please enter an option: "))
        except ValueError:
            print("Invalid input")
            continue

        if menu_option == 1:
            input_num = (input("Please enter your password to encode:  "))
            if len(input_num) == 8 and input_num.isdigit():
                encoded_num = encode(input_num)
                print(f"Your password has been encoded and stored!")
            else:
                print("Invalid input.")
            print("")

        elif menu_option == 2:
            if len(str(encoded_num)) == 8 and str(encoded_num).isdigit():
                input_num = decode(encoded_num)
                print(f"The encoded password is {encoded_num}, and the original password is {input_num}.")
            else:
                print("Invalid input.")
            print()
        elif menu_option == 3:
            break

main()